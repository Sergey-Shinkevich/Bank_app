from collections.abc import generator

import pytest
from src.generators import filter_by_currency, transaction_descriptions

#Тесты функции filter_by_currency
def test_filter_by_currency_empty() -> None:
    """Тестирование на пустой список"""
    generator = filter_by_currency([])
    assert next(generator) == "Пустой список"

def test_filter_by_currency_abnormal_data(abnormal_list_dict_currency) -> None:
    """Тестирование функции на неправильные данные"""
    with pytest.raises(KeyError):
        next(filter_by_currency(abnormal_list_dict_currency))

def test_filter_by_currency_normal_data(normal_list_dict_currency) -> None:
    """Тестирование функции на правильные данные"""
    generator = filter_by_currency(normal_list_dict_currency)
    assert next(generator) == normal_list_dict_currency[0]
    assert next(generator) == normal_list_dict_currency[1]
    assert next(generator) == normal_list_dict_currency[3]

#Тесты функции transaction_descriptions()
def test_transaction_descriptions_empty() -> None:
    """Тестирование на пустой список"""
    generator = transaction_descriptions([])
    assert next(generator) == "Пустой список"

def test_transaction_descriptions_normal_data(normal_list_dict_currency) -> None:
    """Тестирование функции на правильные данные"""
    generator = transaction_descriptions(normal_list_dict_currency)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

def test_transaction_descriptions_abnormal_data(abnormal_list_dict_currency) -> None:
    """Тестирование функции на неправильные данные"""
    generator = transaction_descriptions(abnormal_list_dict_currency)
    assert next(generator) == "Не корректное наименование операции"
    assert next(generator) == "Перевод со счета на счет"
