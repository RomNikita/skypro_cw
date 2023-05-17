import json


def open_json_file():
    with open('../operations.json', 'r', encoding='utf8') as json_file:
        data = json.load(json_file)
        return data


def state_executed():
    file = open_json_file()
    executed_operations = []
    for item in file:
        key = item.get("state")
        if key == "EXECUTED":
            executed_operations.append(item)
    return executed_operations


def right_date():
    operations = state_executed()
    date = []
    for item in operations:
        date_iter = item["date"]
        date_splited = date_iter.split('T')
        normal_date = date_splited[0].split('-')
        return normal_date[::-1]


def mask_number_card():
    pass


def right_description():
    operations = state_executed()
    descriptions = []
    for item in operations:
        descript = item["description"]
        return descript


