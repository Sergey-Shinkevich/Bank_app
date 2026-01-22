def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    card_number_str: str = str(card_number)
    result: str = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[12:]}"
    return result


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    account_number_str: str = str(account_number)
    result: str = f"**{account_number_str[-4:]}"
    return result
