from loguru import logger
from pyrogram import Client, enums
from pyrogram.types import Message
from suvvyapi import Message as SuvvyMessage
from suvvyapi import SuvvyAPIWrapper

from telegram_user_bot.config import Config


async def on_message(client: Client, message: Message, config: Config) -> None:
    logger.info("Received message from {message_sender}", message_sender=f"{message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ' '}".strip())

    await client.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    suvvy = SuvvyAPIWrapper(config.suvvy_api_key)
    response = await suvvy.predict(
        message=SuvvyMessage(text=message.text),
        unique_id=f"suvvyai/telegram-user-bot {message.from_user.id}"
    )
    await message.reply(response.actual_response.text)
