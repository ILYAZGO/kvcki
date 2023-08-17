import pytest
import requests
from utils.create_delete_user import create_user, delete_user
from utils.variables import *

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    width = [1366, 1920, 1440, 1536, 1600]
    height = [768, 1080, 900, 864, 900]


    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }

@pytest.fixture(scope="session", autouse=True)
def users():
    URL = "https://api.stand.imot.io"

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

    token = get_token.json()
    bearer = token['token_type'].capitalize()
    access_token = token['access_token']

    headers_create = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': bearer + " " + access_token,
    }

    headers_delete = {
        'accept': '*/*',
        'Authorization': bearer + " " + access_token,
    }

    user_id_1 = create_user(URL, name1, login1, PASSWORD, headers_create)
    user_id_2 = create_user(URL, name2, login2, PASSWORD, headers_create)
    user_id_3 = create_user(URL, name3, login3, PASSWORD, headers_create)

    # data = {
    #     'role': 'user',
    #     'login': 'qwe',
    #     'name': 'qwe',
    #     'password': 'qwe'
    # }
    # create = requests.post(url=URL + "/user", headers=headers1, json=data)
    # user_id = create.text.replace('"', '')
    #
    # if create.status_code == 200:
    #     print("\nUSERS CREATED SUCCESSFULLY")
    # elif create.status_code == 409:
    #     print("\nUSERS ALREADY CREATED")
    # else:
    #     print("\nwtf")

    yield

    delete_user(URL, user_id_1, headers_delete)
    delete_user(URL, user_id_2, headers_delete)
    delete_user(URL, user_id_3, headers_delete)
    # delete = requests.delete(url=URL + "/user/" + user_id, headers=headers_delete, json=data)
    #
    # if delete.status_code == 204:
    #     print("\nUSERS DELETED")
    # else:
    #     print("\nUSERS NOT DELETED")