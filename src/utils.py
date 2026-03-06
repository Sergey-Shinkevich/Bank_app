import json


def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Строго проверяем, что внутри именно список
            if isinstance(data, list):
                return data
            return []
    except FileNotFoundError, json.JSONDecodeError:
        # Файл не найден или пуст/поврежден (невалидный JSON)
        return []