import requests
import random
import json
import os
import time
from datetime import datetime, timedelta, timezone
from loguru import logger

logger.remove()
logger.add(sink='exec.log', level='INFO', rotation='10 MB', compression='zip', diagnose=True)

'''for create user write before test :
USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, {name}, {login}, PASSWORD)

for delete user write after test :
delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)'''


def create_user(URL, ROLE, PASSWORD):

    NAME = LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H')}_{random.randint(100,99999)}"

    headers_for_get_token = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'username': '4adminIM',
        'password': 'Qaz123wsX',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

    json_for_create = {
        'role': ROLE,
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD,
        "sttOptions": {
            "sttEconomize": False,
            "sttOptionsMap": {}
        }
    }

    get_token = requests.post(url=URL + "/token", headers=headers_for_get_token, data=data).json()

    token = f"{get_token['token_type'].capitalize()} {get_token['access_token']}"

    headers_for_create = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': token,
    }

    create = requests.post(url=URL + "/user", headers=headers_for_create, json=json_for_create)
    user_id = create.text.replace('"', '')

    if create.status_code == 200:
        logger.opt(depth=1).info(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> ERROR CREATE USER {create.status_code} {create.text}<<<<<")

    if ROLE == 'user':

        # giving quota if user
        quota = {
            "time_nominal": 46620
        }

        give_quota = requests.post(url=URL + "/user/" + user_id + "/quota", headers=headers_for_create, json=quota)

        if give_quota.status_code == 200:
            logger.opt(depth=1).info(f"\n>>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 777 MINUTES <<<<<")
        else:
            logger.opt(depth=1).info(f"\n>>>>> ERROR GIVING QUOTA {give_quota.status_code} <<<<<")

        # get token for user and greate group and rule for user

        data_for_user = {
            'username': NAME,
            'password': PASSWORD,
            'scope': '',
            'client_id': '',
            'client_secret': '',
        }
        get_token_for_user = requests.post(url=URL + "/token", headers=headers_for_get_token, data=data_for_user).json()

        token_for_user = f"{get_token_for_user['token_type'].capitalize()} {get_token_for_user['access_token']}"

        headers_for_user = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token_for_user,
        }
        rule_group = {
            "title": "auto_rule_group",
            "enabled": True
        }
        add_rule_group = requests.post(url=URL + "/tag_rule_group/", headers=headers_for_user, json=rule_group)

        group_id = add_rule_group.text.replace('"', '')

        if add_rule_group.status_code == 201:
            logger.opt(depth=1).info(f"\n>>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE GROUP {group_id} <<<<<")
        else:
            logger.opt(depth=1).info(f"\n>>>>> ERROR CREATING RULE GROUP {add_rule_group.status_code} <<<<<")

        rule = {
            "owner": user_id,
            "title": "auto_rule",
            "group": group_id,
            "enabled": True,
            "calculatedRulePriority": 0,
            "globalFilter": [],
            "fragmentRules": [{"phrasesAndDicts": [], "phrases": [], "dicts": [],
                              "direction": "", "fromStart": False, "silentBefore": "",
                              "silentAfter": "", "interruptTime": "", "talkBefore": "",
                               "talkAfter": "", "onlyFirstMatch": False, "fragmentsBefore": "",
                               "fragmentsAfter": "", "distancePrevRuleTime": "", "distancePrevRuleFragmentCount": "",
                               "orPhrasesAndDicts": [], "orPhrases": [], "orDicts": [], "orDirection": ""}],
            "setTags": [{"name": "auto_rule", "value": "", "visible": False}],
            "allowedActions": [],
            "timeTagRules": []}

        add_rule = requests.post(url=URL + "/tag_rule/", headers=headers_for_user, json=rule)

        rule_id = add_rule.text.replace('"', '')

        if add_rule.status_code == 201:
            logger.opt(depth=1).info(f"\n>>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE {rule_id} INSIDE GROUP {group_id} <<<<<")
        else:
            logger.opt(depth=1).info(f"\n>>>>> ERROR CREATING RULE {add_rule.status_code} <<<<<")

        # upload call

        client_audio_path = os.path.join('audio', 'count-in.wav')
        operator_audio_path = os.path.join('audio', 'count-out.wav')

        # time for call
        current_time = datetime.now(timezone.utc)
        delta_ten = current_time + timedelta(minutes=10)
        # delta_one = current_time + timedelta(minutes=1)
        now = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        # one_min_later = delta_one.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        ten_min_later = delta_ten.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        headers_for_upload = {
            'accept': 'application/json',
            'Authorization': token_for_user,
        }

        # json
        json_data = {
            # "operator_filename": "string",
            # "bitrix_deal_id": "string",
            # "telegram_chat_id": "string",
            # "bitrix_crm_phone_number": "string",
            # "stereo_url": "string",
            # "speaker_names": ["first", "second"],
            "unique_id": f"2ceb2380baed63d{random.randint(100000, 999999)}a96",
            # "bitrix_crm_entity_type": "string",
            # "bitrix_crm_entity_id": "string",
            # "bitrix_entity_type": "string",
            # "amo_note_id": "string",
            # "hangup": "client",
            "call_time": now,
            # "stereo_audio_md5": "string",
            # "answer_time": one_min_later ,
            "client_channel": 1,
            "has_audio": True,
            # "telegram_message_id": "string",
            # "bitrix_call_id": "string",
            "end_time": ten_min_later,
            # "amo_url_md5": "string",
            "operator_phone": "1234567890",
            # "operator_url": "string",
            "integration_data": {
                "integration_id": f"63ac6380baed63d{random.randint(100000, 999999)}a96",
                "task_id": f"2c0bfb31-2596-49a3-8a92-19a93dbc078f",
                "service_name": "auto_test"
            },
            "is_only_new_tags": False,
            # "crm_entity_id": "string",
            "unanswered": False,
            # "conversation_id": f"{random.randint(100000,999999)}",
            "is_mono": False,
            # "language": "ru",
            "tags": [
                {
                    "tag_type": "upload",
                    "name": "auto",
                    "value": "test",
                    "visible": True
                }
            ],
            "client_phone": "0987654321",
            # "multichannel_params": [
            #     {
            #         "speaker_name": "Alex",
            #         "is_operator": False,
            #         "unique_id": f"{random.randint(100000,999999)}"
            #     }
            # ],
            # "client_url": "string",
            # "client_filename": "string",
            # "amo_event_id": "string",
            "is_multichannel": False,
            "direction": "income"
        }

        # move json to string
        json_str = json.dumps(json_data)

        params_for_upload = {'params': (None, json_str)}

        upload = requests.post(url=URL + "/call/", headers=headers_for_upload, data=params_for_upload,
                               files=
                               {
                                   'client_audio': ('count-in.wav',
                                                    open(client_audio_path, 'rb'),
                                                    'audio/wav'),
                                   'operator_audio': ('count-out.wav',
                                                      open(operator_audio_path, 'rb'),
                                                      'audio/wav')
                               })

        if upload.status_code == 200:
            logger.opt(depth=1).info(f"\n>>>>> WAV id:{upload.text} uploaded  {URL}/call/ <<<<<")
        else:
            logger.opt(depth=1).info(f"\n>>>>> WAV upload error {upload.status_code} text {upload.text} <<<<<")

        time.sleep(40)


    return user_id, token, LOGIN


def create_operator(URL, PARENT_USER_ID, PASSWORD):

    NAME = LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

    headers_for_get_token = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'username': '4adminIM',
        'password': 'Qaz123wsX',
        'scope': '',
        'client_id': '',
        'client_secret': '',
    }

    json = {
        'role': 'operator',
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD,
        'parentUser': PARENT_USER_ID
    }

    get_token = requests.post(url=URL + "/token", headers=headers_for_get_token, data=data).json()
    token = f"{get_token['token_type'].capitalize()} {get_token['access_token']}"

    headers_for_create = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': token,
    }

    create_operator = requests.post(url=URL + "/user", headers=headers_for_create, json=json)
    user_id = create_operator.text.replace('"', '')

    if create_operator.status_code == 200:
        logger.opt(depth=1).info(f"\n>>>>> OPERATOR {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> ERROR CREATE OPERATOR {create_operator.status_code} <<<<<")

    return user_id, token, LOGIN


def delete_user(URL, token, USER_ID ):

    headers_for_delete = {
        'accept': '*/*',
        'Authorization': token,
    }

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=headers_for_delete)

    if delete.status_code == 204:
        logger.opt(depth=1).info(f"\n>>>>> USER {USER_ID} DELETED <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> USER {USER_ID} NOT DELETED <<<<<")


def give_user_to_manager(URL, USER_ID_MANAGER, USER_ID_USER, token):

    headers_for_giving = {
        'accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    importFrom_id = '64b923905f95f6305573e619'
    json_with_id = [USER_ID_USER, importFrom_id]

    give_user = requests.put(url=URL + "/user/" + USER_ID_MANAGER + "/user_limitation", headers=headers_for_giving, json=json_with_id)


    if give_user.status_code == 204:
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} WAS NOT GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")


def give_manager_all_rights(URL, USER_ID_MANAGER, token ):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    json_with_rights = {'restt': 'true','delete_user': 'true', 'add_user': 'true','set_default_engine': 'true',
            'quota_edit': 'true', 'gpt_quota': 'true','user_modules_setup': 'true'}

    give_rights = requests.put(url=URL + "/user/" + USER_ID_MANAGER + "/access_rights", headers=headers, json=json_with_rights)

    if give_rights.status_code == 204:
        logger.opt(depth=1).info(f"\n>>>>> MANAGER {USER_ID_MANAGER} NOW HAVE ALL RIGHTS <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> MANAGER {USER_ID_MANAGER} FAILED TO GET ALL RIGHTS <<<<<")



