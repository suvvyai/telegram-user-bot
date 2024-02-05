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

    typing_event = asyncio.Event()

    try:
        suvvy = AsyncSuvvyAPIWrapper(config.suvvy_api_key, check_connection=False)

        logger.debug("Sending received message to Suvvy AI...")
        response = await suvvy.predict(
            message=SuvvyMessage(text=message.text),
            unique_id=f"suvvyai/telegram-user-bot {message.from_user.id}",
            raise_if_dialog_stopped=True,
        )
        logger.success("Suvvy AI answered: {text}", text=response.actual_response.text)

        logger.info(
            "Waiting for {before_read} + {before_answer} seconds before replying",
            before_read=config.timeouts.before_read_seconds,
            before_answer=config.timeouts.before_answer_seconds,
        )
        await asyncio.sleep(config.timeouts.before_read_seconds)
        await client.read_chat_history(message.chat.id)
        await asyncio.sleep(config.timeouts.before_answer_seconds)

        asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

        logger.success("Replying!")
        await message.reply(response.actual_response.text)
    except HistoryStoppedError:
        logger.warning("Suvvy AI refused to answer")
    except Exception as e:
        logger.error("Suvvy AI raised an error: {e}", e=e)
    finally:
        typing_event.set()
