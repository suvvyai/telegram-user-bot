from loguru import logger
from pyrogram import Client
from pyrogram.types import Message


async def on_message(message: Message, client: Client) -> None:
    logger.info("Received message from @{message_sender}", message_sender=message.chat.username)
    pass
