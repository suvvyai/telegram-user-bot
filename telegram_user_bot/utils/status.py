import asyncio

from pyrogram.enums import ChatAction


async def typing_action(client, chat_id, duration):
    while duration > 0:
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(4)  # Telegram обновляет статус каждые 5 секунд
        duration -= 4


async def keep_typing(client, chat_id, event: asyncio.Event):
    while not event.is_set():
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        await asyncio.sleep(4)
