import asyncio

from pyrogram import Client
from pyrogram.enums import ChatAction


async def typing_action(client: Client, chat_id: int, duration: int) -> None:
    while duration > 0:
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(4)  # Telegram обновляет статус каждые 5 секунд
        duration -= 4


async def keep_typing(client: Client, chat_id: int, event: asyncio.Event) -> None:
    while not event.is_set():
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(4)
