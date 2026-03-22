import csv

import pandas as pd


def csv_read_to_dict(path: str) -> list[dict]:
    """Функция читает CSV-файл и возвращает список словарей"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            return list(reader)
    except Exception:
        return []


def excel_read_to_dict(path: str) -> list[dict]:
    """Функция читает Excel-файл и возвращает список словарей"""
    try:
        excel_data = pd.read_excel(path)
        result = excel_data.to_dict(orient="records")
        return result
    except Exception:
        return []
