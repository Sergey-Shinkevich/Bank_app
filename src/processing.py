def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state  соответствует указанному значению.
    """
    result: list[dict] = []
    for item in list_dict:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(list_dict: list[dict], up_down: bool = True) -> list[dict]:
    """Функцию сортировки списка словарей по дате. Для направления сортировки - параметр up_down"""
    result = sorted(list_dict, key=lambda list_dict: list_dict["date"], reverse=up_down)
    return result
