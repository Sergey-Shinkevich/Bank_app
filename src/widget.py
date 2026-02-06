from src.masks import get_mask_account, get_mask_card_number


def check_date_format(full_date: str) -> bool:
    """Функция проверки правильности формата даты"""
    if len(full_date) == 26:
        names_digits = [
            full_date[0:4],
            full_date[5:7],
            full_date[8:10],
            full_date[11:13],
            full_date[14:16],
            full_date[17:19],
            full_date[20:],
        ]
        is_correct = True
        for name in names_digits:
            if name.isdigit():
                continue
            else:
                is_correct = False
        if (
            full_date[13] == ":"
            and full_date[16] == ":"
            and full_date[19] == "."
            and full_date[10] == "T"
            and full_date[4] == "-"
            and full_date[7] == "-"
            and is_correct
        ):
            result: bool = True
        else:
            result = False
    else:
        result = False
    return result


def mask_account_card(number_card_or_account: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    incorrect = "Не правильное название карты / счета"
    if number_card_or_account != "":
        split_string: list[str] = number_card_or_account.split()
        words = ["Maestro", "Счет", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]

        if len(split_string) == 2:
            name = split_string[0]
        elif len(split_string) == 3:
            name = " ".join(split_string[0:2])
        else:
            return incorrect

        if name in words:
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


def get_date(full_date: str) -> str:
    """Функция обработки даты в формат ДЕНЬ.МЕСЯЦ.ГОД"""
    if check_date_format(full_date):
        result: str = f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"
    else:
        result = "Не корректная дата"
    return result
