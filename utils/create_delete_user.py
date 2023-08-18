import requests


def get_token(URL):
    headers = {
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
    get_token = requests.post(url=URL + "/token", headers=headers, data=data)

    return get_token

def create_user(URL,NAME,LOGIN,PASSWORD,HEADERS):
    data = {
        'role': 'user',
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD
    }
    create = requests.post(url=URL + "/user", headers=HEADERS, json=data)
    user_id = create.text.replace('"', '')

    if create.status_code == 200:
        print(f"\n>>>>> USER {NAME} WITH user_id: {user_id} CREATED SUCCESSFULLY <<<<<")
    elif create.status_code == 409:
        print(f"\n>>>>> USER {NAME} ALREADY EXISTS <<<<<")
    elif create.status_code == 422:
        print(f"\n>>>>> VALIDATION ERROR 422 <<<<<")
    else:
        print(f"\n>>>>> ACCESS DENIED 403 <<<<<")

    quota = {
        "time_nominal": 7200
    }

    give_quota = requests.post(url=URL + "/user/" + user_id + "/quota", headers=HEADERS, json=quota)

    if give_quota.status_code == 200:
        print(f">>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 120 MINUTES <<<<<")
    else:
        print(f">>>>> ERROR GIVING QUOTA {give_quota.status_code} <<<<<")




    return user_id

def delete_user(URL,USER_ID,HEADERS):

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=HEADERS)

    if delete.status_code == 204:
        print(f"\n>>>>> USER {USER_ID} DELETED <<<<<")
    else:
        print(f"\n>>>>> USER {USER_ID} NOT DELETED <<<<<")