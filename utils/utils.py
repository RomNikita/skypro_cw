import json



def open_json_file(filename):
    """Открывает json file"""

    with open(filename, 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
    return data


def state_executed(json_file):
    """Возвращает все операции со статусом EXECUTED"""
    executed_operations = []
    for item in json_file:
        key = item.get("state")
        if key == "EXECUTED":
            executed_operations.append(item)
    return executed_operations


def sort_by_date(executed_operations):
    """Сортирует операции по дате, с самой новой до самой старой"""
    sort_list = sorted(executed_operations, key=lambda x: x.get("date"), reverse=True)
    return sort_list


def right_date(date):
    """Выводит дату в правильном формате"""
    date_splited = date.split('T') # Делим дату по букве Т
    normal_date = date_splited[0].split('-') # Индекс 0 - это датаЮ разбиваем ее на лист по знаку -
    return '.'.join(normal_date[::-1]) # Возвращает дату с конца и между ними стоит точка


def mask_card(requisites_of_operations: str):
    """Маскирует номер карты или счета"""
    name = '' # Добавил 2 переменные name и number, так как python выдает ошибку
    number = ''
    if requisites_of_operations:
        name = " ".join(requisites_of_operations.split(" ")[:-1]) #Название платежной системы или счет
        number = requisites_of_operations.split(" ")[-1] # Номер карты или счета
    if len(number) == 16: # Если номер равен 16 - это номер карты, масируем это как карту
        mask_number = number[:6] + "*" * 6 + number[12:16]
        number_sep = [mask_number[i:i + 4] for i in range(0, len(number), 4)]
        return f'{name} {" ".join(number_sep)}'
    elif len(number) == 20: # Если символов 20 - это номер счета, маскируем как счет
        return f'{name} {number.replace(number[:-4], "**")}'

    return "Not exist" # Если ничего нет, возвращаем фразу Not exist


def print_last_five_operations(sorted_operations):
    """Возвращает последние 5 операций """
    return sorted_operations[0:5]

