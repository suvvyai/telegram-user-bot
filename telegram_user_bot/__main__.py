from loguru import logger
from pyrogram import Client

from telegram_user_bot.config import config
from telegram_user_bot.handlers import add_handlers
from telegram_user_bot.utils.log import configure_logger


def main() -> None:
    configure_logger()

    client = Client(name=config.session_name, device_model="suvvyai/telegram-user-bot", system_version="Github latest")

    add_handlers(client)
    logger.success("Starting bot...")
    client.run()


if __name__ == "__main__":
    main()
