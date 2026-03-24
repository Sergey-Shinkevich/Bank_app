import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/utils.log",
    filemode="w",
    encoding="utf-8",
)
logger = logging.getLogger("utils")


def read_json(path):
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Чтение файла данных прошло успешно")
            if isinstance(data, list):
                logger.info("Данные являются - JSON")
                return data
            logger.warning("Данные не являются - JSON")
            return []
    except FileNotFoundError:
        logger.error("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка структуры данных JSON")
        return []
