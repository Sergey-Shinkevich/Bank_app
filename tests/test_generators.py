import pytest
from src.generators import filter_by_currency

#Тесты функции filter_by_currency
def test_filter_by_currency_empty() -> None:
    """Тестирование на пустой список"""
    next(filter_by_currency([])) == "Пустой список"

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

#