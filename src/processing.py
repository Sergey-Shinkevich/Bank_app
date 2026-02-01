from src.widget import check_date_format


def check_list_dict(list_dict: list[dict]) -> bool:
    """Проверка целостности данных в списке словарей"""
    if not list_dict:
        return False
    for item in list_dict:
        # Проверка длины и наличия корректных ключей
        if len(item) == 3 and "id" in item and "state" in item and "date" in item:
            current_id = str(item.get("id"))
            current_state = str(item.get("state"))
            current_date = str(item.get("date"))
            if (
                current_id.isdigit()
                and (current_state == "EXECUTED" or current_state == "CANCELED")
                and check_date_format(current_date)
            ):
                continue
            else:
                return False
        else:
            return False
    return True


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


def sort_by_date(list_dict: list[dict], up_down: bool = False) -> list[dict] | str:
    """Функцию сортировки списка словарей по дате. Для направления сортировки создан параметр up_down"""
    if check_list_dict(list_dict):
        result = sorted(list_dict, key=lambda list_dict: list_dict["date"], reverse=up_down)
        return result
    else:
        return "Не верные данные"
