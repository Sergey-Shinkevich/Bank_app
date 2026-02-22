import pytest
from src.decorators import log

import pytest
import os

def test_log_console(capsys):
    """Тест вывода логов в консоль)"""
    @log()
    def multiply(a, b):
        return a * b
    multiply(10, 2)
    captured = capsys.readouterr().out
    assert "Запуск multiply((10, 2), {}) - OK" in captured
    assert "Окончание multiply((10, 2), {}) - 20 - OK" in captured


def test_log_file(tmp_path):
    """Тест записи логов в файл"""
    test_file = tmp_path / "function_logs.txt"
    file_path = str(test_file)
    @log(file=file_path)
    def say_hello(name="User"):
        return f"Hello, {name}"
    say_hello(name="Sky")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert "Запуск say_hello((), {'name': 'Sky'}) - OK" in content
    assert "Окончание say_hello((), {'name': 'Sky'}) - Hello, Sky - OK" in content


def test_log_exception(capsys):
    """Тест логирования ошибки и ее последующего проброса (raise)"""

    @log()
    def fail_func():
        return 1 / 0
    with pytest.raises(ZeroDivisionError):
        fail_func()
    captured = capsys.readouterr().out
    assert "Ошибка fail_func error: division by zero" in captured
