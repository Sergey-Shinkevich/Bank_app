import re


def process_bank_search(data, search):
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    result = []
    for item in data:
        if re.search(search, item.get("description", ""), re.IGNORECASE):
            result.append(item)
    return result
