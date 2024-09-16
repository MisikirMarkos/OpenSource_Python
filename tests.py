import reminder as app
from reminder import Task
import datetime as dt

import pytest


def test_to_date():
    assert app._to_date("2021-09-01") == dt.date(2021, 9, 1)
    with pytest.raises(ValueError, match="is not in YYYY-MM-DD format."):
        app._to_date("2021-09-31")


@pytest.fixture
def task_list():
    return [Task(name="pay rent"), Task(name="buy groceries")]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("buy groceries", Task(name="buy groceries")),
        ("buy apple", None),
        ("PAY RENT", Task(name="pay rent")),
    ],
)
def test_find_task(test_input, expected, task_list):
    assert app._find_task(test_input, task_list) == expected


def test_save_and_load_task_list(task_list):
    app._save_task_list(task_list)
    assert app._get_task_list() == task_list
