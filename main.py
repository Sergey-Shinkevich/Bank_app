from bank_search import process_bank_search
from generators import filter_by_currency
from processing import filter_by_state, sort_by_date
from transaction_reader import csv_read_to_dict, excel_read_to_dict
from utils import read_json
from widget import get_date, mask_account_card


def main():
    """Функция основного запуска программы"""
    # Приветствие, запрос и обработка типа источника информации. Получение информации. Переменная: data
    while True:
        print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла\n")
        choice = input("Пользователь: ")
        if choice == "1":
            type_data = "JSON"
            data = read_json("data/operations.json")
            break
        elif choice == "2":
            type_data = "CSV"
            data = csv_read_to_dict("data/transactions.csv")
            break
        elif choice == "3":
            type_data = "XLSX"
            data = excel_read_to_dict("data/transactions_excel.xlsx")
            break
        print("Программа: Не корректный ввод\n")
    print(f"Программа: Для обработки выбран {type_data}-файл.\n")

    # Ввод и обработка статуса для фильтрации операций.
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input("Пользователь: ").upper()

        if status in ["EXECUTED", "CANCELED", "PENDING"]:
            state_data = filter_by_state(data, status)
            break
        print(f"Программа: Статус операции {status} недоступен.\n")
    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    # Ввод и обработка необходимости сортировки.
    while True:
        print("Программа: Отсортировать операции по дате? Да/Нет")
        is_sort = input("Пользователь: ").upper()
        if is_sort == "ДА":
            is_sort = True
            break
        elif is_sort == "НЕТ":
            is_sort = False
            break

    # Ввод и обработка направления сортировки.
    while True:
        if not is_sort:
            sort_list = state_data
            break
        else:
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            choice = input("Пользователь:").upper()
            if choice == "ПО ВОЗРАСТАНИЮ":
                sort_list = sort_by_date(state_data)
                break
            elif choice == "ПО УБЫВАНИЮ":
                sort_list = sort_by_date(state_data, up_down=True)
                break

    # Обработка фильтра рублевых транзакций
    while True:
        print("Программа: Выводить только рублевые транзакции? Да/Нет")
        choice = input("Пользователь: ").upper()
        if choice == "ДА":
            currency_list = list(filter_by_currency(sort_list, "RUB"))
            break
        elif choice == "НЕТ":
            currency_list = sort_list
            break

    # Фильтрация транзакций по описанию
    while True:
        print("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        choice = input("Пользователь: ").upper()
        if choice == "НЕТ":
            result_list = currency_list
            break
        elif choice == "ДА":
            print("Введите строку для поиска в поле: Описание")
            search_string = input("Пользователь: ")
            result_list = process_bank_search(currency_list, search_string)
            break

    # Вывод результатов
    if result_list == []:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for item in result_list:
            item_date = get_date(item.get("date"))
            item_description = item.get("description")
            print(item_date, item_description)
            if item_description[:8] == "Открытие":
                item_account = item.get("to")
                print(item_account)
            else:
                item_from = mask_account_card(item.get("from"))
                item_to = mask_account_card(item.get("to"))
                print(f"{item_from} -> {item_to}")

            if type_data == "JSON":
                ammount = item["operationAmount"]["amount"]
                сurrency = item["operationAmount"]["currency"]["name"]
                print(f"Сумма: {ammount} {сurrency}")
            else:
                ammount = item.get("amount")
                сurrency = item.get("currency_code", 0)
                print(f"Сумма: {ammount} {сurrency}")
            print("")


if __name__ == "__main__":
    main()
