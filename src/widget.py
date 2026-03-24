from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


@log(file="mylog.txt")
def check_date_format(full_date: str) -> bool:
    """Функция проверки правильности формата даты"""
    names_digits = [full_date[0:4], full_date[5:7], full_date[8:10]]
    is_correct = True
    for name in names_digits:
        if name.isdigit():
            continue
        else:
            is_correct = False
    return is_correct


@log(file="mylog.txt")
def mask_account_card(number_card_or_account: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    incorrect = "Не правильное название карты / счета"
    if number_card_or_account != "":
        split_string: list[str] = number_card_or_account.split()
        words = [
            "maestro",
            "счет",
            "mastercard",
            "visa classic",
            "visa platinum",
            "visa gold",
            "мир",
            "discover",
            "american express",
            "visa",
        ]

        if len(split_string) == 2:
            name = split_string[0]
        elif len(split_string) == 3:
            name = " ".join(split_string[0:2])
        else:
            return incorrect

        if name.lower() in words:
            if split_string[0] == "Счет":
                masked_number: str = get_mask_account(split_string[-1])
            else:
                masked_number = get_mask_card_number(split_string[-1])
            split_string[-1] = masked_number
            result: str = " ".join(split_string)
        else:
            result = incorrect
    else:
        result = incorrect
    return result


@log(file="mylog.txt")
def get_date(full_date: str) -> str:
    """Функция обработки даты в формат ДЕНЬ.МЕСЯЦ.ГОД"""
    if check_date_format(full_date):
        result: str = f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"
    else:
        result = "Не корректная дата"
    return result
