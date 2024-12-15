from utils.create_delete_user import create_user, delete_user, give_user_to_manager, create_operator
from utils.variables import *
from utils.dates import *
import requests
import pytest
import allure
import time
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID


current_date = datetime.now()

today = current_date.strftime("%Y-%m-%d")
today_with_dots = current_date.strftime("%d.%m.%Y")

# class CreateTask(BaseModel):
#     task_id: UUID


def get_token(url: str, login: str, password: str):

    headers_for_get_token = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data_for_user = {
        'username': login,
        'password': password,
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }
    get_token_for_user = requests.post(url=url + "/token", headers=headers_for_get_token, data=data_for_user).json()

    token_for_user = f"{get_token_for_user['token_type'].capitalize()} {get_token_for_user['access_token']}"

    return token_for_user



actions = ["analyze", "apply_gpt", "swap_channels", "get_api_tags", "apply_notify_rules", "apply_addressbook_tags", "delete"]


#@pytest.mark.independent
@pytest.mark.api
@allure.title("test_tasks")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_tasks. parametrize")
@pytest.mark.parametrize("task_type", actions)
def test_tasks(task_type):

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Get token for user"):
        user_token = get_token(API_URL, LOGIN, PASSWORD)

    with allure.step("Give all rights for user"):
        headers_for_rights = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': TOKEN
        }

        data_for_rights = {
            "restt": True,
            "delete_call": True,
            "call_info_processing": True
        }

        give_rights_to_user = requests.put(url=API_URL + f"/user/{USER_ID}/access_rights", headers=headers_for_rights, json=data_for_rights)

    with allure.step("Check status code == 204"):
        assert give_rights_to_user.status_code == 204

    with allure.step("Create task"):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': user_token,
        }

        data = {
            "start_date": today,
            "end_date": today,
            "action": task_type,
        }


        create_task = requests.post(url=API_URL + "/calls/action", headers=headers, json=data)

        task_id = create_task.json()["task_id"]

    with allure.step("Check status code == 200 and we get UUID"):
        assert create_task.status_code == 200
        assert isinstance(UUID(task_id), UUID)  # Ensure it's a UUID instance
        assert UUID(task_id).version == 4  # Check if it's a version 4 UUID

    with allure.step("Sleep 5 sec"):
        time.sleep(5)

    with allure.step("Get tasks"):
        get_progress_tasks = requests.get(url=API_URL + "/progress_tasks", headers=headers)
        json_get_progress_tasks = get_progress_tasks.json()

    with allure.step("Check status code == 200 and response"):
        assert get_progress_tasks.status_code == 200
        assert json_get_progress_tasks[0]["task_id"] == task_id  # check task_id
        assert json_get_progress_tasks[0]["owner"] == USER_ID  # check task belongs to created user
        assert json_get_progress_tasks[0]["status"] == "SUCCESS" # check status
        assert json_get_progress_tasks[0]["action"] == task_type  # check action type
        assert json_get_progress_tasks[0]["progress"] == {}
        assert today in json_get_progress_tasks[0]["add_time"]
        assert today in json_get_progress_tasks[0]["done_time"]
        #assert json_get_progress_tasks[0]["title"] == {}
        #assert json_get_progress_tasks[0]["task_interval"] == f"коммуникации за: {today_with_dots}-{today_with_dots}"
        assert json_get_progress_tasks[0]["total"] == 1
        assert json_get_progress_tasks[0]["current"] == 1

    with allure.step("Get task"):
        get_task_status = requests.get(url=API_URL + f"/task/{task_id}/status", headers=headers)
        json_get_task_status = get_task_status.json()

    with allure.step("Check status code == 200 and response"):
        assert get_task_status.status_code == 200
        assert json_get_task_status["task_id"] == task_id  # check task_id
        assert json_get_task_status["owner"] == USER_ID  # check task belongs to created user
        assert json_get_task_status["status"] == "SUCCESS"  # check status
        assert json_get_task_status["action"] == task_type  # check action type
        assert json_get_task_status["progress"] == {}
        assert today in json_get_task_status["add_time"]
        assert today in json_get_task_status["done_time"]
        # assert json_get_task_status["title"] == {}
        # assert json_get_task_status["task_interval"] == f"коммуникации за: {today_with_dots}-{today_with_dots}"
        assert json_get_task_status["total"] == 1
        assert json_get_task_status["current"] == 1

    with allure.step("Delete task"):
        delete_task = requests.delete(url=API_URL + f"/task/{task_id}", headers=headers)

    with allure.step("Check that status code == 204"):
        assert delete_task.status_code == 204

    with allure.step("Get tasks and check status code == 200 and []"):
        get_progress_tasks = requests.get(url=API_URL + "/progress_tasks", headers=headers)

        assert  get_progress_tasks.status_code == 200
        assert get_progress_tasks.json() == []

