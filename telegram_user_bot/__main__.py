import json

from pyrogram import Client
from loguru import logger
import click

from telegram_user_bot.config import Config


@click.command()
@click.option("--config", "-c", type=click.Path(exists=True, dir_okay=False, readable=True), required=True)
def main(config: str):
    config = Config(**json.loads(open(config, "r", encoding='utf-8').read()))
    logger.success("Loaded config from {config_path}", config_path=config)

    logger.info("Authorizing with given user phone number...")
    client = Client(name=f"users/{config.phone_number.strip('+ ')}", api_id=config.api_id, api_hash=config.api_hash, phone_number=config.phone_number)
    logger.success("Successfully authorized!")


if __name__ == '__main__':
    main()
