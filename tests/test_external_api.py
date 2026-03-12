from unittest.mock import patch

import requests

from src.external_api import api_key, bank_transaction_amount


@patch("src.external_api.requests.get")
def test_external_api_normal_usd(mock_get):
    """Проверка на конвертацию функции из USD в RUB"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1772981648, "rate": 79.26285},
        "date": "2026-03-08",
        "result": 2533048.869903,
    }
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert bank_transaction_amount(transaction) == 2533048.87
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=31957.58",
        headers={"apikey": api_key},
    )


@patch("src.external_api.requests.get")
def test_external_api_normal_eur(mock_get):
    """Проверка на конвертацию функции из EUR в RUB"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1772981648, "rate": 79.26285},
        "date": "2026-03-08",
        "result": 2533048.869903,
    }
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert bank_transaction_amount(transaction) == 2533048.87
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=31957.58",
        headers={"apikey": api_key},
    )


def test_external_api_normal_abnormal():
    """Проверка на конвертацию функции из неопределенной валюты"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "JPY", "code": "JPY"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert bank_transaction_amount(transaction) == 0.0


def test_external_api_normal_rub():
    """Проверка на подсчет суммы в рублях"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert bank_transaction_amount(transaction) == 31957.58


@patch("src.external_api.requests.get")
def test_external_api_status(mock_get):
    """Обработка ошибок №1"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Mocked HTTP error")
    result = bank_transaction_amount(transaction)
    assert result == 0.0
    mock_get.return_value.raise_for_status.assert_called_once()


@patch("src.external_api.requests.get")
def test_external_api_key_error(mock_get):
    """Неправильный запрос"""
    mock_get.return_value.json.return_value = {"status": "success", "something_else": 123}
    mock_get.return_value.status_code = 200

    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = bank_transaction_amount(transaction)
    assert result == 0.0
