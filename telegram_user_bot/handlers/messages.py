from loguru import logger
from pyrogram import Client
from pyrogram.types import Message


async def on_message(client: Client, message: Message) -> None:
    logger.info("Received message from {message_sender}", message_sender=f"{message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name else ' '}".strip())
    pass
