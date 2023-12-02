import asyncio

from loguru import logger
from pyrogram import Client, enums
from pyrogram.types import Message
from suvvyapi import Message as SuvvyMessage, AsyncSuvvyAPIWrapper
from suvvyapi.exceptions.api import HistoryStoppedError

from telegram_user_bot.config import Config
from telegram_user_bot.utils.log import send_message_log
from telegram_user_bot.utils.status import keep_typing


async def on_message(client: Client, message: Message, config: Config) -> None:
    await asyncio.sleep(config.timeouts.before_read_seconds)
    await client.read_chat_history(message.chat.id)
    await asyncio.sleep(config.timeouts.before_answer_seconds)

    typing_event = asyncio.Event()

    asyncio.create_task(keep_typing(client, message.chat.id, typing_event))

    suvvy = AsyncSuvvyAPIWrapper(config.suvvy_api_key, check_connection=False)

    try:
        response = await suvvy.predict(
            message=SuvvyMessage(text=message.text),
            unique_id=f"suvvyai/telegram-user-bot {message.from_user.id}",
            raise_if_dialog_stopped=True
        )

        typing_event.set()
        await message.reply(response.actual_response.text)

        send_message_log(
            full_name=f"{message.from_user.first_name}{f' {message.from_user.last_name}' if message.from_user.last_name is not None else ''}",
            text=message.text,
            username=message.from_user.username,
            answer=response.actual_response.text
        )
    except HistoryStoppedError:
        send_message_log(
            full_name=f"{message.from_user.first_name}{f' {message.from_user.last_name}' if message.from_user.last_name is not None else ''}",
            text=message.text,
            username=message.from_user.username,
            answer="Dialog is intercepted (202)"
        )
