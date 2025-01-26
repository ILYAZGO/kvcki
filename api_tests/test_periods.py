from utils.create_delete_user import create_user, delete_user
from utils.variables import *
from utils.dates import *
from api_tests.common import *
import requests
import pytest
import allure
import time
from datetime import datetime


period = ["yesterday", "today", "this_week", "last_week", "this_month", "last_month",
          "this_quarter", "last_quarter", "this_year", "last_year", "all_time"]


@pytest.mark.api
@allure.title("test_periods")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_periods. parametrize")
@pytest.mark.parametrize("period_type", period)
def test_periods(period_type):
    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Get token for user"):
        user_token = get_token(API_URL, LOGIN, PASSWORD)

    with allure.step("Create operator by user"):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': user_token,
        }

    with allure.step("Get period"):
        get_period = requests.get(url=API_URL + f"/get_date_range_by_period?period={period_type}", headers=headers)

    with allure.step("Check status code == 200"):
        assert get_period.status_code == 200
        if period_type == "yesterday":
            assert get_period.text == f'["{yesterday.strftime("%Y-%m-%d")}","{yesterday.strftime("%Y-%m-%d")}"]'
        elif period_type == "today":
            assert get_period.text == f'["{today.strftime("%Y-%m-%d")}","{today.strftime("%Y-%m-%d")}"]'
        elif period_type == "this_week":
            assert get_period.text == f'["{first_day_this_week.strftime("%Y-%m-%d")}","{last_day_this_week.strftime("%Y-%m-%d")}"]'
        elif period_type == "last_week":
            assert get_period.text == f'["{first_day_last_week.strftime("%Y-%m-%d")}","{last_day_last_week.strftime("%Y-%m-%d")}"]'
        elif period_type == "this_month":
            assert get_period.text == f'["{first_day_this_month.strftime("%Y-%m-%d")}","{last_day_this_month.strftime("%Y-%m-%d")}"]'



        elif period_type == "last_year":
            assert get_period.text == f'["{first_day_last_year.strftime("%Y-%m-%d")}","{last_day_last_year.strftime("%Y-%m-%d")}"]'
        elif period_type == "this_year":
            assert get_period.text == f'["{first_day_this_year.strftime("%Y-%m-%d")}","{last_day_this_year.strftime("%Y-%m-%d")}"]'
