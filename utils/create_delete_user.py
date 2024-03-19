import requests
from datetime import datetime

'''for create user write before test :
USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, {name}, {login}, PASSWORD)

for delete user write after test :
delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)'''


def create_user(URL, ROLE, PASSWORD):

    NAME = LOGIN = f"auto_test_user_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

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
        print(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    elif create.status_code == 409:
        print(f"\n>>>>> USER {NAME} ALREADY EXISTS <<<<<")
    elif create.status_code == 422:
        print(f"\n>>>>> VALIDATION ERROR 422 <<<<<")
    else:
        print(f"\n>>>>> ACCESS DENIED 403 <<<<<")

    #quota = {
    #    "time_nominal": 1800
    #}

    #give_quota = requests.post(url=URL + "/user/" + user_id + "/quota", headers=headers_for_create, json=quota)

    #if give_quota.status_code == 200:
    #    print(f">>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 777 MINUTES <<<<<")
    #else:
    #    print(f">>>>> ERROR GIVING QUOTA {give_quota.status_code} <<<<<")

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

    create = requests.post(url=URL + "/user", headers=headers_for_create, json=json)
    user_id = create.text.replace('"', '')

    if create.status_code == 200:
        print(f"\n>>>>> OPERATOR {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    elif create.status_code == 409:
        print(f"\n>>>>> OPERATOR {NAME} ALREADY EXISTS <<<<<")
    elif create.status_code == 422:
        print(f"\n>>>>> VALIDATION ERROR 422 <<<<<")
    else:
        print(f"\n>>>>> ACCESS DENIED 403 <<<<<")

    return user_id, token, LOGIN


def delete_user(URL, token, USER_ID ):

    headers_for_delete = {
        'accept': '*/*',
        'Authorization': token,
    }

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=headers_for_delete)

    if delete.status_code == 204:
        print(f"\n>>>>> USER {USER_ID} DELETED <<<<<")
    else:
        print(f"\n>>>>> USER {USER_ID} NOT DELETED <<<<<")


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
        print(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} GIVED TO MANAGER {USER_ID_MANAGER} <<<<<")
    else:
        print(f"\n>>>>> USERS {USER_ID_USER}  and {importFrom_id} WAS NOT GIVED TO MANAGER {USER_ID_MANAGER}<<<<<")




