from mypy.binder import Iterator


def filter_by_currency(trans, curr="RUB"):
    """Генератор транзакций по фильтру валюты"""
    for item in trans:
        # 1. Пытаемся достать валюту из JSON (сложная структура)
        # Мы используем .get(), чтобы программа не "падала", если ключа нет
        op_amount = item.get("operationAmount")
        if isinstance(op_amount, dict):
            currency_info = op_amount.get("currency", {})
            # Проверяем и 'code' (RUB) и 'name' (руб.)
            val = currency_info.get("code") or currency_info.get("name")
        else:
            # 2. Если это не словарь (значит, это CSV или Excel), берем плоский ключ
            val = item.get("currency_code") or item.get("currency_name") or item.get("currency")

        # 3. Сравниваем то, что нашли, с нашим запросом (RUB)
        # Приводим к верхнему регистру и убираем пробелы для надежности
        if val:
            val_str = str(val).upper().strip()
            curr_str = str(curr).upper().strip()

            # Если ищем рубли, проверяем оба варианта (код и название)
            if curr_str == "RUB" or curr_str == "РУБ":
                if val_str in ["RUB", "РУБ", "РУБ."]:
                    yield item
            # Для всех остальных валют (USD, EUR) обычное сравнение
            elif curr_str == val_str:
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
    result = ((" ".join(number[i : i + 4] for i in range(0, len(number), 4))) for number in long_string)
    for card in result:
        yield card
