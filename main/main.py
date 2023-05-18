from utils.utils import state_executed, right_date, right_description
import json

def main():
    operations = state_executed()
    for item in operations:
        date = right_date()
        description = right_description()
        return f"{date[0]}.{date[1]}.{date[2]} {description}"


print(main())