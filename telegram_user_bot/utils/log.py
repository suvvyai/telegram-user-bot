import datetime
import sys

from loguru import logger


def configure_logger() -> None:
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> {exception}"

    logger.remove()
    logger.add(sys.stdout, colorize=True, format=log_format, diagnose=True, backtrace=True)
    logger.add("logs/log.log", rotation="1 week", diagnose=True, enqueue=True, colorize=True, backtrace=True)
    logger.level("DEBUG", color="<fg #7f7f7f>")
    logger.level("INFO", color="<white>")
    logger.level("SUCCESS", color="<green>")
    logger.level("WARNING", color="<yellow>")
    logger.level("ERROR", color="<red>")
    logger.level("CRITICAL", color="<bold><white><RED>")


def send_message_log(full_name: str, text: str, answer: str, username: str | None = None) -> None:
    text = f"""New message:
    👤 {full_name} {f"(@{username})" if username else ""}
    🕓 At {datetime.datetime.now()}
    💬 Text:
{text}
    🤖 Answer:
{answer}
    """
    logger.info(text)
