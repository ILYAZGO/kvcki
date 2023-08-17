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
        print("\nUSER CREATED SUCCESSFULLY")
    elif create.status_code == 409:
        print("\nUSER ALREADY CREATED")
    else:
        print("\nwtf")

    return user_id

def delete_user(URL,USER_ID,HEADERS):

    delete = requests.delete(url=URL + "/user/" + USER_ID, headers=HEADERS)

    if delete.status_code == 204:
        print("\nUSER DELETED")
    else:
        print("\nUSER NOT DELETED")