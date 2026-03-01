from src.decorators import log


@log(file="mylog.txt")
def get_mask_card_number(card_number: str | int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number_str: str = str(card_number)
    if len(card_number_str) == 16 and card_number_str.isdigit():
        result: str = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
    else:
        result = "Не правильный номер карты"
    return result


@log(file="mylog.txt")
def get_mask_account(account_number: str | int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    account_number_str: str = str(account_number)
    if len(account_number_str) >= 6 and account_number_str.isdigit():
        result: str = f"**{account_number_str[-4:]}"
    else:
        result = "Не правильный номер счета"
    return result
