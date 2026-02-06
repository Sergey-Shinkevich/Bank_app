from src.processing import check_list_dict, filter_by_state, sort_by_date


# Проверка функции check_list_dict
def test_list_dict_empty(empty_list: list) -> None:
    """Проверка на пустой список"""
    assert check_list_dict(empty_list) is False


def test_normal_data(normal_list_dict: list[dict]) -> None:
    """Проверка на правильные данные"""
    assert check_list_dict(normal_list_dict) is True


def test_abnormal_data_01(abnormal_list_dict_01: list[dict]) -> None:
    """Проверка на не правильные данные №1"""
    assert check_list_dict(abnormal_list_dict_01) is False


def test_abnormal_data_02(abnormal_list_dict_02: list[dict]) -> None:
    """Проверка на не правильные данные №2"""
    assert check_list_dict(abnormal_list_dict_02) is False


def test_abnormal_data_03(abnormal_list_dict_03: list[dict]) -> None:
    """Проверка на не правильные данные №3"""
    assert check_list_dict(abnormal_list_dict_03) is False


def test_abnormal_data_04(abnormal_list_dict_04: list[dict]) -> None:
    """Проверка на не правильные данные №4"""
    assert check_list_dict(abnormal_list_dict_04) is False


# Проверка функции filter_by_state
def test_executed(normal_list_dict: list[dict]) -> None:
    assert filter_by_state(normal_list_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_canceled(normal_list_dict: list[dict]) -> None:
    assert filter_by_state(normal_list_dict, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Проверка функции sort_by_date
def test_sort_date_low(normal_list_dict: list[dict]) -> None:
    assert sort_by_date(normal_list_dict) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


def test_sort_date_high(normal_list_dict: list[dict]) -> None:
    assert sort_by_date(normal_list_dict, up_down=True) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
