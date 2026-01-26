def filter_by_state(list_dict: list[dict], state: str ='EXECUTED' ) -> list[dict]:
    """
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state  соответствует указанному значению.
    """
    result: list[dict] = []
    for item in list_dict:
        if item.get('state') == state:
            result.append(item)
    return result

