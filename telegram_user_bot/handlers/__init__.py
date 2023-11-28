from pyrogram import Client
from pyrogram.handlers import MessageHandler

from telegram_user_bot.handlers.messages import on_message


def add_handlers(app: Client):
    app.add_handler(MessageHandler(on_message))
