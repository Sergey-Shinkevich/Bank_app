from mypy.binder import Iterator


def filter_by_currency(trans: list[dict], curr: str="USD") -> Iterator:
    """Генератор транзакций по фильтру валюты"""
    # Проверка на пустой список
    if len(trans) == 0:
        yield "Пустой список"

    else:
        for item in trans:
            if item["operationAmount"]["currency"]["name"] == curr:
                yield item

def transaction_descriptions(trans: list[dict]) -> str:
    if len(trans) == 0:
        yield "Пустой список"
    else:
        correct_strings = {"Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"}
        for item in trans:
            if item["description"] in correct_strings:
                yield item["description"]
            else:
                yield "Не корректное наименование операции"
