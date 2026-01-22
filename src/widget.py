import masks

def mask_account_card(number_card_or_account:str) -> str:
    """Функция обрабатывает информацию о картах и о счетах"""
    split_string:list[str] = number_card_or_account.split()
    if split_string[0] == "Счет":
        masked_number:str = masks.get_mask_account(split_string[-1])
    else:
        masked_number:str = masks.get_mask_card_number(split_string[-1])
    split_string[-1] = masked_number
    result:str = " ".join(split_string)
    return result

first_test = "Visa Platinum 7000792289606361"
first_test_result = mask_account_card(first_test)
print(first_test)
print(first_test_result)
print()

second_test = "Maestro 7000792289606361"
second_test_result = mask_account_card(second_test)
print(second_test)
print(second_test_result)
print()

third_test = "Счет 73654108430135874305"
third_test_result = mask_account_card(third_test)
print(third_test)
print(third_test_result)
