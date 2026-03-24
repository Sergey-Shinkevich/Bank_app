from collections import Counter


def process_bank_operations(data, categories):
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    descriptions = []
    for item in data:
        if item.get("description") in categories:
            descriptions.append(item.get("description"))
    return dict(Counter(descriptions))
