import sys

from loguru import logger


def configure_logger():
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    logger.remove()
    logger.add(sys.stdout, colorize=True, format=log_format, diagnose=True, backtrace=False)
    logger.add(sys.stderr, backtrace=False, colorize=True, diagnose=True)
    logger.add("logs/log.log", rotation="1 week", diagnose=True, enqueue=True, colorize=True, backtrace=True)
    logger.level("DEBUG", color="<fg #7f7f7f>")
    logger.level("INFO", color="<white>")
    logger.level("SUCCESS", color="<green>")
    logger.level("WARNING", color="<yellow>")
    logger.level("ERROR", color="<red>")
    logger.level("CRITICAL", color="<bold><white><RED>")
