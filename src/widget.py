import masks


def mask_account_card(number_card_or_account: str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    split_string: list[str] = number_card_or_account.split()
    if split_string[0] == "Счет":
        masked_number: str = masks.get_mask_account(split_string[-1])
    else:
        masked_number = masks.get_mask_card_number(split_string[-1])
    split_string[-1] = masked_number
    result: str = " ".join(split_string)
    return result


def get_date(full_date: str) -> str:
    """Функция обработки даты в формат ДЕНЬ.МЕСЯЦ.ГОД"""
    result: str = f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"
    return result
