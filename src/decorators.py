import time
from functools import wraps


def log(file=None):
    """Декоратор указывает время начала работы функции, окончания работы функций,
    названия функции, аргументов и результатов выполнения"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                log_info = f"{time.ctime()} Запуск {func.__name__}({args}, {kwargs}) - OK\n"
                output_log(log_info)
                result = func(*args, **kwargs)
                log_info = f"{time.ctime()} Окончание {func.__name__}({args}, {kwargs}) - {result} OK\n"
                output_log(log_info)
                return result
            except Exception as e:
                log_info = f"{time.ctime()} Ошибка {func.__name__} error: {e}. Inputs {args}, {kwargs}\n"
                output_log(log_info)

        def output_log(log_info):
            """Вспомогательная функция для вывода на экран или в консоль"""
            if file is None:
                print(log_info)
            else:
                with open(file, "a", encoding="utf-8") as f:
                    f.write(log_info)

        return wrapper

    return decorator
