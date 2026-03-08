import os
import requests
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

def bank_transaction_amount(transaction):
    """Функция для возвращает сумму транзакции в рублях"""
    currency = transaction['operationAmount']['currency']['code']
    if  currency == 'RUB':
        res = transaction['operationAmount']['amount']
        amount = float(res)
        return amount
    elif currency in ['USD', 'EUR']:
        res = transaction['operationAmount']['amount']
        to = "RUB"
        from_ = currency
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={res}"
        headers = {"apikey": api_key}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            result = response.json()
            return round((float(result["result"])), 2)
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return 0.0
        except requests.exceptions.RequestException as err:
            print(f"Other error occurred: {err}")
            return 0.0
        except KeyError:
            print("Unexpected response format")
            return 0.0
    else:
        return 0.0

# Операция в рублях
#print(bank_transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))
# Операция в долларах
#print(bank_transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))
# Операция в евро
#print(bank_transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'EUR.', 'code': 'EUR'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))
# Операция в йене
#print(bank_transaction_amount({'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'JPY', 'code': 'JPY'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}))