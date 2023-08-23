import requests


'''for create user write before test :
USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, {name}, {login}, PASSWORD)

for delete user write after test :
delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)'''



def create_user(URL,NAME,LOGIN,PASSWORD):
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
        'role': 'user',
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD
    }


    get_token = requests.post(url=URL + "/token", headers=headers_for_get_token, data=data)

    token = get_token.json()
    bearer = token['token_type'].capitalize()
    access_token = token['access_token']

    headers_for_create = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': bearer + " " + access_token,
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

    # quota = {
    #     "time_nominal": 7200
    # }
    #
    # give_quota = requests.post(url=URL + "/user/" + user_id + "/quota", headers=headers_for_create, json=quota)
    #
    # if give_quota.status_code == 200:
    #     print(f">>>>> USER {NAME} WITH user_id: {user_id} IS GIVEN A QUOTA OF 120 MINUTES <<<<<")
    # else:
    #     print(f">>>>> ERROR GIVING QUOTA {give_quota.status_code} <<<<<")

    return user_id, bearer, access_token



def delete_user(URL,USER_ID, BEARER, ACCESS_TOKEN):

    headers_for_delete = {
        'accept': '*/*',
        'Authorization': BEARER + " " + ACCESS_TOKEN,
    }

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=headers_for_delete)

    if delete.status_code == 204:
        print(f"\n>>>>> USER {USER_ID} DELETED <<<<<")
    else:
        print(f"\n>>>>> USER {USER_ID} NOT DELETED <<<<<")