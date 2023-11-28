import asyncio
import json

from pyrogram import Client
from loguru import logger
import click

from telegram_user_bot.config import Config
from telegram_user_bot.handlers import add_handlers


@click.command()
@click.option("--config", "-c", type=click.Path(exists=True, dir_okay=False, readable=True), default="config.json")
def main(config: str = "config.json") -> None:
    config_path = config
    config = Config(**json.loads(open(config_path, "r", encoding='utf-8').read()))
    logger.success("Loaded config from {config_path}", config_path=config_path)
    client = Client(name=f"{config.phone_number.strip('+ ')}", api_id=config.api_id, api_hash=config.api_hash,
                    phone_number=config.phone_number, device_model="Python", system_version="suvvyai/telegram-user-bot 0.1")

    add_handlers(client)
    logger.success("Starting bot...")
    client.run()


if __name__ == '__main__':
    main()
