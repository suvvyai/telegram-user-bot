import asyncio
import json

from pyrogram_patch import patch

from pyrogram import Client
from loguru import logger
import click

from telegram_user_bot.config import Config
from telegram_user_bot.handlers import add_handlers
from telegram_user_bot.middlewares.value import ParamValueMiddleware


@click.command()
@click.option("--config", "-c", type=click.Path(exists=True, dir_okay=False, readable=True), default="config.json")
def main(config: str = "config.json") -> None:
    config_path = config
    config = Config(**json.loads(open(config_path, "r", encoding='utf-8').read()))
    logger.success("Loaded config from {config_path}", config_path=config_path)

    client = Client(name=config.session_name, device_model="suvvyai/telegram-user-bot", system_version="Github latest")

    patch_manager = patch(client)
    patch_manager.include_middleware(ParamValueMiddleware(key="config", value=config))

    add_handlers(client)
    logger.success("Starting bot...")
    client.run()


if __name__ == '__main__':
    main()
