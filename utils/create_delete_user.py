import requests
def create_user(URL,LOGIN,NAME,PASSWORD,HEADERS):
    data = {
        'role': 'user',
        'login': LOGIN,
        'name': NAME,
        'password': PASSWORD
    }
    create = requests.post(url=URL + "/user", headers=HEADERS, json=data)
    user_id = create.text.replace('"', '')

    if create.status_code == 200:
        print(f"\n>>>>> USER {NAME } CREATED SUCCESSFULLY <<<<<")
    elif create.status_code == 409:
        print(f"\n>>>>> USER {NAME} ALREADY EXISTS <<<<")
    elif create.status_code == 422:
        print(f"\n>>>>> VALIDATION ERROR 422 <<<<")
    else:
        print(f"\n>>>>> ACCESS DENIED 403 <<<<")

    return user_id

def delete_user(URL,USER_ID,HEADERS):

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=HEADERS)

    if delete.status_code == 204:
        print(f"\n>>>>> USER {USER_ID} DELETED <<<<")
    else:
        print(f"\n>>>>> USER {USER_ID} NOT DELETED <<<<")