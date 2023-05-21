from utils.utils import right_date, mask_card, sort_by_date, print_last_five_operations, open_json_file, state_executed
import json

json_file = open_json_file("../operations.json")
executed_operations = state_executed(json_file)
sorted_operations = sort_by_date(executed_operations)
operations = print_last_five_operations(sorted_operations)


for item in operations:
    print(f'{right_date(item.get("date"))} {item.get("description")}\n'
          f'{mask_card(item.get("from"))} -> {mask_card(item.get("to"))}\n'
          f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n')

