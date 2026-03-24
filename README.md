# Учебный проект банковского гаджета
____
## Установка
Приложение можно установить скачав его по адресу:

https://github.com/Sergey-Shinkevich/Bank_app
____
## Зависимости
+ python 3.12
+ black 26.1.0
+ flake8 7.3.0
+ isort 7.0.0
+ mypy 1.19.1
+ pytest 9.0.2
+ pytest-cov 7.0.0
+ python-dotenv 1.2.2
+ requests 2.32.5
+ pandas 3.0.1
+ openpyxl 3.1.5
+ pandas-stubs 3.0.0.260204
____
## Описание функциональных возможностей
- **get_mask_card_number** - принимает на вход номер карты и возвращает ее маску.
- **get_mask_account** - принимает на вход номер счета и возвращает его маску.
- **check_list_dict** - осуществляет проверку на целостность списка словарей.
- **filter_by_state** - возвращает новый список словарей, содержащий только те словари, 
у которых ключ state соответствует указанному значению.
- **sort_by_date** - сортирует словари по дате.
- **read_json** - читает локальный JSON файл.
- **check_date_format** - проверяет правильность формата даты.
- **mask_account_card** - обрабатывает информацию о картах и о счетах.
- **get_date** - преобразует дату в формат ДЕНЬ.МЕСЯЦ.ГОД.
- **log** - декоратор осуществляющий логирование.
- **bank_transaction_amount** - возвращает сумму транзакции в рублях.
- **filter_by_currency** - генератор транзакций по фильтру валюты.
- **transaction_descriptions** - возвращает описание каждой операции по очереди. 
- **card_number_generator** - генератор номеров банковских карт.
- **csv_read_to_dict** - Функция читает CSV-файл и возвращает список словарей.
- **excel_read_to_dict** - Функция читает Excel-файл и возвращает список словарей.
- **process_bank_operations** - Функция принимает список словарей с данными о банковских 
операциях и список категорий операций, возвращает словарь, в котором ключи - это названия 
категорий, а значения - это количество операций в каждой категории.
- **process_bank_search** - Функция принимает список словарей с данными о банковских 
операциях и строку поиска, а возвращает список словарей, у которых в описании есть данная 
строка.
____
## Покрытие тестами
```
Name                               Stmts   Miss  Cover
------------------------------------------------------
src\__init__.py                        0      0   100%
src\bank_operations.py                 7      0   100%
src\bank_search.py                     7      0   100%
src\decorators.py                     23      0   100%
src\external_api.py                   32      2    94%
src\generators.py                     29      2    93%
src\masks.py                          25      0   100%
src\processing.py                     24      3    88%
src\transaction_reader.py             16      0   100%
src\utils.py                          20      0   100%
src\widget.py                         37      1    97%
tests\__init__.py                      0      0   100%
tests\conftest.py                     22      0   100%
tests\test_bank_operations.py          5      0   100%
tests\test_bank_search.py              7      0   100%
tests\test_decorator.py               29      0   100%
tests\test_external_api.py            36      0   100%
tests\test_generators.py              33      0   100%
tests\test_masks.py                   19      0   100%
tests\test_proccesing.py              13      0   100%
tests\test_transaction_reader.py      30      0   100%
tests\test_utils.py                   22      0   100%
tests\test_widget.py                  21      0   100%
------------------------------------------------------
TOTAL                                457      8    98%
```