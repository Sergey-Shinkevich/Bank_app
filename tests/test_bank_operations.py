from src.bank_operations import process_bank_operations


def test_process_bank_operations_valid(normal_list_dict_currency):
    """Обычный тест функции при существующем и не существующем значении"""
    assert process_bank_operations(normal_list_dict_currency, ["Перевод организации", "Оплата связи"]) == {
        "Перевод организации": 2
    }


def test_process_bank_operations_empty_list(normal_list_dict_currency):
    """Тест функции при пустом списке"""
    assert process_bank_operations(normal_list_dict_currency, []) == {}
