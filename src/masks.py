import logging

from src.decorators import log

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/masks.log",
    filemode="w",
    encoding="utf-8",
)
logger_number = logging.getLogger("get_mask_card_number")
logger_account = logging.getLogger("get_mask_account")


@log(file="mylog.txt")
def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number_str: str = str(card_number)
    logger_number.info(f"Номер {card_number_str} прочитан")
    if len(card_number_str) == 16 and card_number_str.isdigit():
        result: str = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
        logger_number.info(f"Результат {result}")
    else:
        result = "Не правильный номер карты"
        logger_number.warning(f"Не правильный номер: {card_number_str}")
    return result


@log(file="mylog.txt")
def get_mask_account(account_number: str | int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    account_number_str: str = str(account_number)
    if len(account_number_str) >= 6 and account_number_str.isdigit():
        logger_account.info(f"Данные {account_number} верны")
        result: str = f"**{account_number_str[-4:]}"
        logger_account.info(f"Результат {result}")
    else:
        result = "Не правильный номер счета"
        logger_account.warning(f"Не правильный номер счета {account_number}")
    return result
