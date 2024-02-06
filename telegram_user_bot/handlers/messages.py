import asyncio

from loguru import logger
from pyrogram import Client
from pyrogram.types import Message
from suvvyapi import AsyncSuvvyAPIWrapper
from suvvyapi import Message as SuvvyMessage
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
        asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

        logger.info(
            "Waiting for {before_answer} seconds before replying",
            before_answer=config.timeouts.before_answer_seconds,
        )

        await asyncio.sleep(config.timeouts.before_answer_seconds)

    typing_event = asyncio.Event()

    try:
        suvvy = AsyncSuvvyAPIWrapper(config.suvvy_api_key, check_connection=False)

        logger.info("Faking user activity...")
        fake_type_task = asyncio.create_task(fake_type())

        logger.debug("Sending received message to Suvvy AI...")
        response = await suvvy.predict(
            message=SuvvyMessage(text=message.text),
            unique_id=f"suvvyai/telegram-user-bot {message.from_user.id}",
            raise_if_dialog_stopped=True,
        )
        logger.success("Suvvy AI answered: {text}", text=response.actual_response.text)

        if not fake_type_task.done():
            await fake_type_task

        logger.success("Replying!")
        await message.reply(response.actual_response.text)
    except HistoryStoppedError:
        logger.warning("Suvvy AI refused to answer")
    except Exception as e:
        logger.error("Suvvy AI raised an error: {e}", e=e)
    finally:
        typing_event.set()
