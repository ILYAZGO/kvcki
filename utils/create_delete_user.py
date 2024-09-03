import requests
import random
from datetime import datetime
from loguru import logger

logger.remove()
logger.add(sink='exec.log', level='INFO', rotation='10 MB', compression='zip', diagnose=True)

'''for create user write before test :
USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, {name}, {login}, PASSWORD)

for delete user write after test :
delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)'''


def create_user(URL, ROLE, PASSWORD):

    NAME = LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{random.randint(100,999)}"

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
        'role': ROLE,
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD
    }

    get_token = requests.post(url=URL + "/token", headers=headers_for_get_token, data=data).json()

    token = f"{get_token['token_type'].capitalize()} {get_token['access_token']}"

    headers_for_create = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': token,
    }

    create = requests.post(url=URL + "/user", headers=headers_for_create, json=json)
    user_id = create.text.replace('"', '')

    if create.status_code == 200:
        logger.opt(depth=1).info(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> ERROR CREATE USER {create.status_code} <<<<<")

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


        # # send audio file
        # headers_for_audio = {
        #     'accept': 'application/json',
        #     'Content-Type': 'multipart/form-data',
        #     'Authorization': token_for_user,
        # }
        #
        # parameters = {"operator_filename": "string", "bitrix_deal_id": "string", "telegram_chat_id": "string",
        #               "bitrix_crm_phone_number": "string", "stereo_url": "string", "speaker_names": ["string"],
        #               "unique_id": "string", "bitrix_crm_entity_type": "string", "bitrix_crm_entity_id": "string",
        #               "bitrix_entity_type": "string", "amo_note_id": "string", "hangup": "client",
        #               "call_time": "2024-09-02T09:34:29.349Z", "stereo_audio_md5": "string",
        #               "answer_time": "2024-09-02T09:34:29.349Z", "client_channel": "0", "has_audio": "true",
        #               "telegram_message_id": "string", "bitrix_call_id": "string",
        #               "end_time": "2024-09-02T09:34:29.349Z",
        #               "amo_url_md5": "string", "operator_phone": "string", "operator_url": "string",
        #               "integration_data": {"integration_id": "string", "task_id": "string", "service_name": "string"},
        #               "is_only_new_tags": "false", "crm_entity_id": "string", "unanswered": "false",
        #               "conversation_id": "string", "is_mono": "false", "language": "string",
        #               "tags": [{"tag_type": "upload", "name": "string", "value": "string", "visible": "true"}],
        #               "client_phone": "string",
        #               "multichannel_params": [{"speaker_name": "string", "is_operator": "false", "unique_id": "string"}],
        #               "client_url": "string", "client_filename": "string", "amo_event_id": "string",
        #               "is_multichannel": "false", "direction": "income"}


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
    json = [USER_ID_USER, importFrom_id]

    give_user = requests.put(url=URL + "/user/" + USER_ID_MANAGER + "/user_limitation", headers=headers_for_giving, json=json)


    if give_user.status_code == 204:
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")
    else:
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} WAS NOT GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")




