from mypy.binder import Iterator


def filter_by_currency(trans: list[dict], curr: str = "USD") -> Iterator:
    """Генератор транзакций по фильтру валюты"""
    # Проверка на пустой список
    if len(trans) == 0:
        yield "Пустой список"

    else:
        for item in trans:
            if item["operationAmount"]["currency"]["name"] == curr:
                yield item


def transaction_descriptions(trans: list[dict]) -> Iterator:
    """Функция возвращает описание каждой операции по очереди"""
    if len(trans) == 0:
        yield "Пустой список"
    else:
        correct_strings = {"Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"}
        for item in trans:
            if item["description"] in correct_strings:
                yield item["description"]
            else:
                yield "Не корректное наименование операции"


def card_number_generator(start: int, stop: int) -> Iterator:
    """Функция-генератор номеров банковских карт"""
    long_string = [(16 - len(str(x))) * "0" + str(x) for x in range(start, stop + 1)]
    result = ((" ".join(number[i: i + 4] for i in range(0, len(number), 4))) for number in long_string)
    for card in result:
        yield card
