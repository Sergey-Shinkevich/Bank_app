import pytest

from src.widget import check_date_format, get_date, mask_account_card


# Тесты функции mask_account_card()
def test_empty_input(empty: str) -> None:
    """Проверка на пустой ввод"""
    assert mask_account_card(empty) == "Не правильное название карты / счета"


@pytest.mark.parametrize(
    "number, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_normal_data(number: str, result: str) -> None:
    """Проверка работоспособности функции при правильных значениях"""
    assert mask_account_card(number) == result


@pytest.mark.parametrize(
    "number, result",
    [
        ("Maestro Cчет 1596837868705199", "Не правильное название карты / счета"),
        ("Счет ", "Не правильное название карты / счета"),
        ("7158300734726758", "Не правильное название карты / счета"),
        ("Visa Maestro 6831982476737658", "Не правильное название карты / счета"),
    ],
)
def test_abnormal_data(number: str, result: str) -> None:
    """Проверка работоспособности функции при не правильных значениях"""
    assert mask_account_card(number) == result


# Тесты функции check_date_format()
def test_empty_date(empty: str) -> None:
    """Проверка на пустой ввод"""
    assert check_date_format(empty) is False


@pytest.mark.parametrize(
    "date, result",
    [
        ("2019-07-03T18:35:29.5123641", True),
        ("20A9-07-03T18:35:29.512364", False),
        ("2019107103T18:35:29.512364", True),
        ("2019-07-03T18635:29.512364", True),
        ("2019-07-03T18:35729.512364", True),
        ("2019-07-03T18:35:297512364", True),
    ],
)
def test_abnormal_date(date: str, result: bool) -> None:
    """Проверка работоспособности функции при не правильных значениях"""
    assert check_date_format(date) == result


@pytest.mark.parametrize(
    "date, result",
    [
        ("2024-03-11T02:26:18.671407", True),
        ("2018-06-30T02:08:58.425572", True),
        ("2019-07-03T18:35:29.512364", True),
    ],
)
def test_normal_date(date: str, result: bool) -> None:
    """Проверка работоспособности функции при не правильных значениях"""
    assert check_date_format(date) == result


# Тесты функции get_date()
@pytest.mark.parametrize(
    "date, result",
    [
        ("2023-07-25T02:26:18.671407", "25.07.2023"),
        ("2012-03-10T02:08:58.425572", "10.03.2012"),
        ("2015-02-05T18:35:29.512364", "05.02.2015"),
    ],
)
def test_short_date(date: str, result: bool) -> None:
    """Проверка работоспособности функции"""
    assert get_date(date) == result
