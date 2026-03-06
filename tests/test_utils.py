from unittest.mock import patch

from src.utils import read_json


def test_read_json_fake_path():
    """Проверка на не существующий файл"""
    with patch("json.load") as mock_load:
        mock_load.return_value = ""
        assert read_json("fake_path.json") == []


def test_read_json_fake_content():
    """Проверка на не JSON-файл"""
    with patch("json.load") as mock_load:
        mock_load.return_value = {"key": "value"}
        assert read_json("fake_content.json") == []


def test_read_json_normal_content():
    """Проверка на не JSON-файл"""
    with patch("json.load") as mock_load:
        mock_load.return_value = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
        ]
        assert read_json("normal.json") == []
