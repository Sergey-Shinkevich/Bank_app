import json
from unittest.mock import mock_open, patch

from src.utils import read_json


def test_read_json_not_found():
    """Проверка: если файла нет, возвращаем пустой список"""
    # Имитируем, что open кидает FileNotFoundError
    with patch("builtins.open", side_effect=FileNotFoundError):
        assert read_json("non_existent.json") == []


def test_read_json_invalid_format():
    """Проверка: если файл — не список (например, словарь)"""
    # Мокаем и открытие файла, и результат json.load
    with patch("builtins.open", mock_open(read_data='{"key": "value"}')):
        with patch("json.load") as mock_load:
            mock_load.return_value = {"key": "value"}
            assert read_json("file.json") == []


def test_read_json_valid():
    """Проверка: если в файле корректный список транзакций"""
    test_data = [{"id": 1, "amount": "100"}]
    with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
        with patch("json.load") as mock_load:
            mock_load.return_value = test_data
            # Тут мы ждем именно наши данные, а не пустой список!
            assert read_json("normal.json") == test_data


def test_read_json_decode_error():
    """Проверка: если файл битый (JSONDecodeError)"""
    with patch("builtins.open", mock_open(read_data="invalid json")):
        with patch("json.load") as mock_load:
            mock_load.side_effect = json.JSONDecodeError("msg", "doc", 0)
            assert read_json("bad.json") == []
