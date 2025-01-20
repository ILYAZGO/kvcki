from utils.create_delete_user import create_user, delete_user
from utils.variables import *
from api_tests.common import *
import requests
import pytest
import allure
import time

available_directions = ["Telegram","Email","API"]

@pytest.mark.api
@allure.title("test_create_update_delete_email_notification_rule")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("test_create_update_delete_email_notification_rule")
def test_create_update_delete_email_notification_rule():

    rule_name = "auto_api_test_email"
    direction = available_directions[1]

    with allure.step("Create user"):
        USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    with allure.step("Get token for user"):
        user_token = get_token(API_URL, LOGIN, PASSWORD)

    with allure.step("Get call_id from today's search calls"):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': user_token,
        }

    with allure.step("Get available directions"):
        get_available_directions = requests.get(url=API_URL + "/notify_rules/available_directions", headers=headers)

    with allure.step("Check available directions status code == 200 and list"):
        assert get_available_directions.status_code == 200
        assert get_available_directions.json() == available_directions

    with allure.step("Check notify rule variables"):
        get_notify_rule_variables = requests.get(url=API_URL + "/notify_rules/notify_rule_variables", headers=headers)
        json_get_notify_rule_variables = get_notify_rule_variables.json()

    with allure.step("Check status code == 200 and content"):
        expected_keys_call_vars = {
            "call_id", "client_phone", "operator_phone", "call_time", "call_timestamp",
            "duration", "unique_id", "conversation_id", "call_points", "call_max_points",
            "link", "link_old", "link_new", "public_link", "public_link_old", "public_link_new",
            "get_fragments('tag_name', 2, 2)", "get_all_text(1000)", "in_line()", "get_stt_json()"
        }
        expected_keys_descriptions = {
            "call_id", "client_phone", "operator_phone", "call_time", "call_timestamp",
            "duration", "unique_id", "conversation_id", "call_points", "call_max_points",
            "link", "public_link", "get_fragments('tag_name', 2, 2)",
            "get_all_text(1000)", "in_line()", "get_stt_json()"
        }
        actual_keys_call_vars = set(json_get_notify_rule_variables["call_vars"].keys())
        actual_keys_descriptions = set(json_get_notify_rule_variables["descriptions"].keys())

        assert get_notify_rule_variables.status_code == 200
        assert json_get_notify_rule_variables["call_vars"]
        assert json_get_notify_rule_variables["descriptions"]
        assert actual_keys_call_vars == expected_keys_call_vars
        assert actual_keys_descriptions == expected_keys_descriptions

    with allure.step("Get notify rules empty list "):
        get_notify_rules_list = requests.get(url=API_URL + "/notify_rules/", headers=headers)

        assert get_notify_rules_list.status_code == 200
        assert get_notify_rules_list.text == "[]"

    with allure.step("Create email notify rule"):
        rule_payload = {
            "owner":USER_ID,
            "title":rule_name,
            "enabled":True,
            "cloneParent":"",
            "activeTgChats":[],
            "tgBody":"",
            "tgAudio":False,
            "emailDst":rule_name,
            "emailSubject":"auto_api_test_email_subject",
            "emailBody":rule_name,
            "apiUrl":"",
            "apiMethod":"",
            "apiResend":False,
            "allowOwerwriteFields":False,
            "apiHeaders":"",
            "apiBody":"",
            "amoNotifyEnabled":True,
            "amoBody":"",
            "amoContactFields":{},
            "amoLeadFields":{},
            "bitrixContactFields":{},
            "bitrixLeadFields":{},
            "bitrixDealFields":{},
            "bitrixBody":"",
            "bitrixNotificationDirection":"",
            "globalFilter":{
                "title":rule_name,
                "items":[{"key":"search_by_tags","logic":"and","complexValues":[{"name":"auto_rule"}]}]},
            "direction":direction}

        create_notify_rule = requests.post(url=API_URL + "/notify_rules/", headers=headers, json=rule_payload)
        notify_rule_id = create_notify_rule.text.replace('"', '')

    with allure.step("Check status code == 200 and rule_id in response"):
        assert create_notify_rule.status_code == 200
        assert len(notify_rule_id) == 24

    with allure.step("Get notify rules list with created notify rule"):
        get_notify_rules_list = requests.get(url=API_URL + "/notify_rules/", headers=headers)

        rule_description = [
            {
                "id":notify_rule_id,
                "owner":USER_ID,
                "title":rule_name,
                "enabled":True,
                "cloneParent":None,
                "direction":direction
            }
        ]

        assert get_notify_rules_list.status_code == 200
        assert get_notify_rules_list.json() == rule_description

    with allure.step("Update notify rule"):
        rule_payload["title"] = "updated_title"
        rule_payload["apiMethod"] = "POST"
        update_notify_rule = requests.put(url=API_URL + f"/notify_rules/{notify_rule_id}", headers=headers, json=rule_payload)

    with allure.step("Check status code == 204"):
        assert update_notify_rule.status_code == 204

    with allure.step("Get notify rules list with updated value"):
        get_notify_rules_list = requests.get(url=API_URL + "/notify_rules/", headers=headers)

        rule_description_updated = [
            {
                "id": notify_rule_id,
                "owner": USER_ID,
                "title": "updated_title",
                "enabled": True,
                "cloneParent": None,
                "direction": direction
            }
        ]

        assert get_notify_rules_list.status_code == 200
        assert get_notify_rules_list.json() == rule_description_updated

    with allure.step("Delete notify rule"):
        delete_notify_rule = requests.delete(url=API_URL + f"/notify_rules/{notify_rule_id}", headers=headers)

    with allure.step("Check status code == 204"):
        assert delete_notify_rule.status_code == 204

    with allure.step("Get empty notify rules list"):
        get_notify_rules_list = requests.get(url=API_URL + "/notify_rules/", headers=headers)

        assert get_notify_rules_list.status_code == 200
        assert get_notify_rules_list.text == "[]"

    with allure.step("Delete user"):
        delete_user(API_URL, TOKEN, USER_ID)