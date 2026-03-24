import pytest
from mypy.binder import Iterator

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тесты функции filter_by_currency
def test_filter_by_currency_empty() -> None:
    """Тестирование на пустой список"""
    result = list(filter_by_currency([]))
    assert result == []


def test_filter_by_currency_abnormal_data(abnormal_list_dict_currency: list[dict]) -> None:
    """Тестирование функции на пропуск неправильных данных"""
    result = list(filter_by_currency(abnormal_list_dict_currency))
    assert len(result) == 0


def test_filter_by_currency_normal_data(normal_list_dict_currency: list[dict]) -> None:
    """Тестирование функции на правильные данные"""
    result = list(filter_by_currency(normal_list_dict_currency, "RUB"))
    assert len(result) == 2
    # Проверяем, что в каждом результате действительно рубли
    for item in result:
        # Проверяем либо через вложенный JSON, либо через плоский ключ
        val = item.get("operationAmount", {}).get("currency", {}).get("code") or item.get("currency_code")
        assert val in ["RUB", "РУБ", "РУБ."]


# Тесты функции transaction_descriptions()
def test_transaction_descriptions_empty() -> None:
    """Тестирование на пустой список"""
    generator: Iterator = transaction_descriptions([])
    assert next(generator) == "Пустой список"


def test_transaction_descriptions_normal_data(normal_list_dict_currency: list[dict]) -> None:
    """Тестирование функции на правильные данные"""
    generator: Iterator = transaction_descriptions(normal_list_dict_currency)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_transaction_descriptions_abnormal_data(abnormal_list_dict_currency: list[dict]) -> None:
    """Тестирование функции на неправильные данные"""
    generator: Iterator = transaction_descriptions(abnormal_list_dict_currency)
    assert next(generator) == "Не корректное наименование операции"
    assert next(generator) == "Перевод со счета на счет"


# Тесты функции card_number_generator
@pytest.mark.parametrize(
    "digit, result",
    [
        (1, "0000 0000 0000 0001"),
        (2, "0000 0000 0000 0002"),
        (3, "0000 0000 0000 0003"),
        (4, "0000 0000 0000 0004"),
        (5, "0000 0000 0000 0005"),
    ],
)
def test_card_number_generator(digit: int, result: str) -> None:
    """Тест генератора карт"""
    generator_card: Iterator = card_number_generator(digit, digit)
    assert next(generator_card) == result
