from utils.create_delete_user import create_user, delete_user
from utils.variables import *
from utils.dates import *
from api_tests.common import get_token
import requests
import pytest
import allure
from datetime import datetime


@pytest.mark.api
@allure.title("test_create_update_delete_employee_positive")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_create_update_delete_employee_positive")
def test_create_update_delete_employee_positive():
    NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    CHANGED_OPERATOR_LOGIN = f"auto_test_operator_changed{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

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

        json = {
            "role":"operator",
            "login":NEW_OPERATOR_LOGIN,
            "name":NEW_OPERATOR_LOGIN,
            "email":NEW_OPERATOR_LOGIN,
            "password":PASSWORD,
            "comment":NEW_OPERATOR_LOGIN,
            "parentUser":USER_ID,
            "phoneNumber":NEW_OPERATOR_LOGIN
        }

        create_operator = requests.post(url=API_URL + "/user", headers=headers, json=json)
        operator_id = create_operator.text.replace('"', '')

    with allure.step("Check status code == 200 and we get operator_id in response"):
        assert create_operator.status_code == 200
        assert len(operator_id) == 24 # check len of created operator id with "

    with allure.step("Get operators list"):
        get_operators = requests.get(url=API_URL + f"/user/{USER_ID}/operators", headers=headers)

    with allure.step("Check status code == 200 and json is correct"):
        json_operators = [
            {
                "id": operator_id,
                "role": "operator",
                "login": NEW_OPERATOR_LOGIN,
                "name": NEW_OPERATOR_LOGIN,
                "timezone": None,
                "parentUser": USER_ID,
                "createdBy": USER_ID,
                "partner": None,
                "industry": None,
                "comment": NEW_OPERATOR_LOGIN,
                "useBilling": False,
                "lanbillingInfo": None,
                "email": NEW_OPERATOR_LOGIN,
                "phoneNumber": NEW_OPERATOR_LOGIN,
                "password": "**********",
                "language": "ru",
                "sttOptions": None,
                "defaultSttOptions": {},
                "sttLanguage": None,
                "enableGpt": None,
                "publicLinkAge": None
            }
        ]

        assert get_operators.status_code == 200
        assert get_operators.json() == json_operators

    with allure.step("Change operator info"):
        json_for_change = {
            "id":operator_id,
            "role":"operator",
            "login":NEW_OPERATOR_LOGIN,   #user cant change login for operator
            "name":CHANGED_OPERATOR_LOGIN,
            "timezone":"",
            "email":CHANGED_OPERATOR_LOGIN,
            "phoneNumber":CHANGED_OPERATOR_LOGIN,
            "password":"**********",
            "comment":CHANGED_OPERATOR_LOGIN,
            "language":"ru",
            "industry":"",
            "partner":"",
            "useBilling":False,
            "lanbillingInfo":None}

        patch_operator = requests.patch(url=API_URL + f"/user/{operator_id}", headers=headers, json=json_for_change)

    with allure.step("Check that operator updated"):
        assert patch_operator.status_code == 204

    with allure.step("Get operators list"):
        get_operators = requests.get(url=API_URL + f"/user/{USER_ID}/operators", headers=headers)

    with allure.step("Check status code == 200 and json is correct"):
        json_operators_after_change = [
            {
                "id": operator_id,
                "role": "operator",
                "login": NEW_OPERATOR_LOGIN,
                "name": CHANGED_OPERATOR_LOGIN,
                "timezone": "",
                "parentUser": USER_ID,
                "createdBy": USER_ID,
                "partner": None,
                "industry": None,
                "comment": CHANGED_OPERATOR_LOGIN,
                "useBilling": False,
                "lanbillingInfo": None,
                "email": CHANGED_OPERATOR_LOGIN,
                "phoneNumber": CHANGED_OPERATOR_LOGIN,
                "password": "**********",
                "language": "ru",
                "sttOptions": None,
                "defaultSttOptions": {},
                "sttLanguage": None,
                "enableGpt": None,
                "publicLinkAge": None
            }
        ]

        assert get_operators.status_code == 200
        assert get_operators.json() == json_operators_after_change


    with allure.step("Delete created operator"):
        delete_operator = requests.delete(url=API_URL + f"/user/{operator_id}", headers=headers)

    with allure.step("Check status code == 204"):
        assert delete_operator.status_code == 204

    with allure.step("Get operators list"):
        get_operators = requests.get(url=API_URL + f"/user/{USER_ID}/operators", headers=headers)

    with allure.step("Check status code == 200"):
        assert get_operators.status_code == 200
        assert get_operators.text == "[]"

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)


@pytest.mark.api
@allure.title("test_create_update_delete_employee_positive")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_create_update_delete_employee_positive")
def est_create_employee_negotive():
    NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"
    CHANGED_OPERATOR_LOGIN = f"auto_test_operator_changed{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

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

        json = {
            "role":"operator",
            "login":"",
            "name":"",
            "email":"",
            "password":"",
            "comment":"",
            "parentUser":USER_ID,
            "phoneNumber":""
        }

        create_operator = requests.post(url=API_URL + "/user", headers=headers, json=json)
        operator_id = create_operator.text.replace('"', '')
        print(operator_id)

    with allure.step("Check status code == 200 and we get operator_id in response"):
        assert create_operator.status_code == 200
        assert len(operator_id) == 24 # check len of created operator id with "

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)