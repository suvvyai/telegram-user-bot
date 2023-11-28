import asyncio

from loguru import logger
from pyrogram import Client, enums
from pyrogram.types import Message
from suvvyapi import Message as SuvvyMessage, AsyncSuvvyAPIWrapper

from telegram_user_bot.config import Config
from telegram_user_bot.utils.status import keep_typing


async def on_message(client: Client, message: Message, config: Config) -> None:
    logger.info("Received message from {message_sender} - \"{text}\"",
                message_sender=f"{message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ' '}".strip(),
                text=message.text
                )

    await asyncio.sleep(config.timeouts.before_read_seconds)
    await client.read_chat_history(message.chat.id)
    await asyncio.sleep(config.timeouts.before_answer_seconds)

    typing_event = asyncio.Event()

    asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

    suvvy = AsyncSuvvyAPIWrapper(config.suvvy_api_key, check_connection=False)
    response = await suvvy.predict(
        message=SuvvyMessage(text=message.text),
        unique_id=f"suvvyai/telegram-user-bot {message.from_user.id}"
    )

    typing_event.set()
    await message.reply(response.actual_response.text)
