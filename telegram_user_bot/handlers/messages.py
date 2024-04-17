import asyncio
import mimetypes
from io import BytesIO
from urllib.parse import quote

import magic
from loguru import logger
from pyrogram import Client
from pyrogram.types import Message
from suvvyapi import Message as SuvvyMessage
from suvvyapi import Suvvy
from suvvyapi.exceptions.api import HistoryStoppedError
from suvvyapi.models.enums import ContentType, SenderRole
from suvvyapi.models.files import Base64File
from suvvyapi.models.messages.content.audio import AudioContent, AudioMessageData
from suvvyapi.models.messages.content.text import TextMessageData

from telegram_user_bot.config import config
from telegram_user_bot.utils.status import keep_typing


async def on_message(client: Client, message: Message) -> None:
    logger.info(
        "Message received from {user}",
        user=f"{message.from_user.first_name}"
        f"{f' {message.from_user.last_name}' if message.from_user.last_name is not None else ''}",
    )

    if message.from_user.is_bot:
        logger.info("Message is from bot. Skipping")
        return

    if message.from_user.is_self:
        logger.info("Message is from self. Skipping")
        return

    async def fake_type() -> None:
        logger.info(
            "Waiting for {before_read} seconds before reading",
            before_read=config.timeouts.before_read_seconds,
        )
        await asyncio.sleep(config.timeouts.before_read_seconds)
        await client.read_chat_history(message.chat.id)

        logger.info(
            "Waiting for {before_type} seconds before typing",
            before_type=config.timeouts.before_typing_seconds,
        )
        await asyncio.sleep(config.timeouts.before_typing_seconds)
        _ = asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

        logger.info(
            "Waiting for {before_answer} seconds before replying",
            before_answer=config.timeouts.before_answer_seconds,
        )

        await asyncio.sleep(config.timeouts.before_answer_seconds)

        logger.info("Replying!")

    typing_event = asyncio.Event()

    try:
        messages: list[SuvvyMessage] = []
        if message.voice is not None:
            logger.info("Caught audio message")
            audio_io = await message.download(file_name="audio.ogg", in_memory=True)
            if isinstance(audio_io, BytesIO):
                audio_io.seek(0)
                messages.append(
                    SuvvyMessage(
                        message_sender=SenderRole.CUSTOMER,
                        message_data=AudioMessageData(
                            content=AudioContent(base64_file=Base64File.from_bytes(audio_io.read()))
                        ),
                    )
                )
        if message.text or message.caption:
            logger.info("Caught text message: {text}", text=message.text or message.caption)
            messages.append(
                SuvvyMessage(
                    message_sender=SenderRole.CUSTOMER,
                    message_data=TextMessageData(content=message.text or message.caption),
                )
            )

        if len(messages) == 0:
            return

        suvvy = Suvvy(config.suvvy_api_key)

        logger.info("Faking user activity...")
        fake_type_task = asyncio.create_task(fake_type())

        logger.debug("Sending received message to Suvvy AI...")
        new_messages, _ = await suvvy.apredict_history_add_message(
            message=messages,
            unique_id=f"suvvyai-telegram-user-bot {message.from_user.id}",
        )
        logger.success("Suvvy AI answered: {new_messages}", new_messages=new_messages)

        if not fake_type_task.done():
            await fake_type_task

        for m in new_messages:
            if m.message_data.data_type is not ContentType.TEXT:
                continue
            logger.success("Replying with {m}", m=m)
            await message.reply(m.message_data.content)
    except HistoryStoppedError:
        logger.warning("Suvvy AI refused to answer")
    except Exception as e:
        logger.error("Suvvy AI raised an error: {e}", e=e)
        logger.exception(e)
    finally:
        typing_event.set()
