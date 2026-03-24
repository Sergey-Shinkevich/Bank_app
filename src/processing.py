from src.decorators import log


@log(file="mylog.txt")
def check_list_dict(list_dict: list) -> bool:
    """Упрощенная проверка: это список и в нем есть словари"""
    # Если это вообще не список или он пустой — работать не с чем
    if not isinstance(list_dict, list) or len(list_dict) == 0:
        return False

    # Проверяем только первый элемент, чтобы не тратить время на перебор тысяч строк
    # и убеждаемся, что это словарь
    if isinstance(list_dict[0], dict):
        return True

    return False


@log(file="mylog.txt")
def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict] | str:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    if check_list_dict(list_dict):
        result: list[dict] = []
        for item in list_dict:
            if item.get("state") == state:
                result.append(item)
    else:
        return "Не верные данные"
    return result


@log(file="mylog.txt")
def sort_by_date(list_dict: list[dict], up_down: bool = False) -> list[dict] | str:
    """Функцию сортировки списка словарей по дате. Для направления сортировки создан параметр up_down"""
    if check_list_dict(list_dict):
        result = sorted(list_dict, key=lambda list_dict: list_dict["date"], reverse=up_down)
        return result
    else:
        return "Не верные данные"
