import asyncio
from urllib.parse import quote

from loguru import logger
from pyrogram import Client
from pyrogram.types import Message
from suvvyapi import Message as SuvvyMessage
from suvvyapi import Suvvy
from suvvyapi.exceptions.api import HistoryStoppedError

from telegram_user_bot.config import config
from telegram_user_bot.utils.status import keep_typing


async def on_message(client: Client, message: Message) -> None:
    logger.info(
        "Message received from {user}",
        user=f"{message.from_user.first_name}"
        f"{f' {message.from_user.last_name}' if message.from_user.last_name is not None else ''}",
    )
    logger.info("Message received: {text}", text=message.text)

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
        await asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

        logger.info(
            "Waiting for {before_answer} seconds before replying",
            before_answer=config.timeouts.before_answer_seconds,
        )

        await asyncio.sleep(config.timeouts.before_answer_seconds)

    typing_event = asyncio.Event()

    try:
        suvvy = Suvvy(config.suvvy_api_key)

        logger.info("Faking user activity...")
        fake_type_task = asyncio.create_task(fake_type())

        logger.debug("Sending received message to Suvvy AI...")
        new_messages, _ = await suvvy.apredict_history_add_message(
            message=message.text,
            unique_id=f"suvvyai-telegram-user-bot {message.from_user.id}",
        )
        logger.success("Suvvy AI answered: {new_messages}", new_messages=new_messages)

        if not fake_type_task.done():
            await fake_type_task

        logger.success("Replying!")
        for m in new_messages:
            if not m.is_visible():
                continue
            await message.reply(m.message_data.content)
    except HistoryStoppedError:
        logger.warning("Suvvy AI refused to answer")
    except Exception as e:
        logger.error("Suvvy AI raised an error: {e}", e=e)
    finally:
        typing_event.set()
