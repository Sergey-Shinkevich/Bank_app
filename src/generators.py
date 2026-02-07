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

