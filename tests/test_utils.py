from utils.utils import open_json_file, state_executed, sort_by_date, mask_card, right_date, print_last_five_operations
from json import JSONDecodeError

import pytest
import json

test_file = open_json_file('tests/tests_data/correct_json.json')
executed_file = open_json_file('tests/tests_data/executed_file.json')


def test_open_json_file():
    assert open_json_file("tests/tests_data/correct_json.json") == []
    with pytest.raises(JSONDecodeError):
        assert open_json_file('tests/tests_data/no_correct.json')

def test_state_executed():
    assert state_executed(test_file) == []
    assert state_executed(executed_file) == \
           [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041"
           }]




def test_right_date():
    assert right_date("2019-08-26T10:50:58.294041") == '26.08.2019'

def test_mask_card():
    assert mask_card('Maestro 0000000000000000') == 'Maestro 0000 00** **** 0000'
    assert mask_card('Счет 64686473678894779589') == 'Счет **9589'
    assert mask_card('') == 'Not exist'


def test_sort_by_date():
    test_date = [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-09-26T10:50:58.294041"},
                 {"date": "2020-08-26T10:50:58.294041"}]

    assert sort_by_date(test_date) == [{"date": "2020-08-26T10:50:58.294041"}, {"date": "2019-09-26T10:50:58.294041"},
                                       {"date": "2019-08-26T10:50:58.294041"}]
    assert sort_by_date(test_file) == []


def test_print_last_five_operations():
    assert print_last_five_operations(test_file) == []
    assert print_last_five_operations([1,2,3,4,5,6]) == [1,2,3,4,5]