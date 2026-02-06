import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты функции get_mask_card_number()
def test_card_empty_number(empty: str) -> None:
    """Проверка на пустой ввод"""
    assert get_mask_card_number(empty) == "Не правильный номер карты"


@pytest.mark.parametrize(
    "number, result", [("1234567890123456", "1234 56** **** 3456"), (1234567890123456, "1234 56** **** 3456")]
)
def test_card_data_types(number: str | int, result: str) -> None:
    """Проверка работоспособности функции при входных данных типа Int и Str"""
    assert get_mask_card_number(number) == result


@pytest.mark.parametrize(
    "number, result", [("1", "Не правильный номер карты"), ("12345678901234567890", "Не правильный номер карты")]
)
def test_card_incorrect_len(number: str | int, result: str) -> None:
    """Проверка, на правильность длины номера карты"""
    assert get_mask_card_number(number) == result


def test_card_is_digit(abnormal_chars: str) -> None:
    """Проверка, что введенные данные состоят из цифр"""
    assert get_mask_card_number(abnormal_chars) == "Не правильный номер карты"


# Тесты функции get_mask_account()
def test_account_empty_number(empty: str) -> None:
    """Проверка на пустой ввод"""
    assert get_mask_account(empty) == "Не правильный номер счета"


@pytest.mark.parametrize("number, result", [("1234567890123456", "**3456"), (1234567890123456, "**3456")])
def test_correct_account_types(number: str | int, result: str) -> None:
    """Проверка работоспособности функции при входных данных типа Int и Str"""
    assert get_mask_account(number) == result


def test_account_is_digit(abnormal_chars: str) -> None:
    """Проверка, что введенные данные состоят из цифр"""
    assert get_mask_account(abnormal_chars) == "Не правильный номер счета"
