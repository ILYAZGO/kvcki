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
        #print(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
        logger.opt(depth=1).info(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    else:
        #print(f"\n>>>>> ACCESS DENIED 403 <<<<<")
        logger.opt(depth=1).info(f"\n>>>>> ERROR CREATE USER {create.status_code} <<<<<")

    if ROLE == 'user':

        # giving quota if user
        quota = {
            "time_nominal": 46620
        }

        give_quota = requests.post(url=URL + "/user/" + user_id + "/quota", headers=headers_for_create, json=quota)

        if give_quota.status_code == 200:
            #print(f">>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 777 MINUTES <<<<<")
            logger.opt(depth=1).info(f"\n>>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 777 MINUTES <<<<<")
        else:
            #print(f">>>>> ERROR GIVING QUOTA {give_quota.status_code} <<<<<")
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
            #print(f">>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE GROUP {group_id} <<<<<")
            logger.opt(depth=1).info(f"\n>>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE GROUP {group_id} <<<<<")
        else:
            #print(f">>>>> ERROR CREATING RULE GROUP {add_rule_group.status_code} <<<<<")
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
            #print(f">>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE {rule_id} INSIDE GROUP {group_id} <<<<<")
            logger.opt(depth=1).info(f"\n>>>>> FOR USER {NAME} WITH user_id: {user_id} CREATED RULE {rule_id} INSIDE GROUP {group_id} <<<<<")
        else:
            #print(f">>>>> ERROR CREATING RULE {add_rule.status_code} <<<<<")
            logger.opt(depth=1).info(f"\n>>>>> ERROR CREATING RULE {add_rule.status_code} <<<<<")

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
        #print(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")
    else:
        #print(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} WAS NOT GIVED TO MANAGER {USER_ID_MANAGER}<<<<<")
        logger.opt(depth=1).info(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} WAS NOT GIVED TO MANAGER {USER_ID_MANAGER}<<<<<")




