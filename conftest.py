import pytest
import requests
from utils.create_delete_user import create_user, delete_user, get_token
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
    token = get_token(API_URL).json()
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

    user_id_1 = create_user(API_URL, name1, login1, PASSWORD, headers_create)
    user_id_2 = create_user(API_URL, name2, login2, PASSWORD, headers_create)
    user_id_3 = create_user(API_URL, name3, login3, PASSWORD, headers_create)
    user_id_4 = create_user(API_URL, name4, login4, PASSWORD, headers_create)
    user_id_5 = create_user(API_URL, name5, login5, PASSWORD, headers_create)
    user_id_6 = create_user(API_URL, name_usedesk, login_usedesk, PASSWORD, headers_create)

    yield

    delete_user(API_URL, user_id_1, headers_delete)
    delete_user(API_URL, user_id_2, headers_delete)
    delete_user(API_URL, user_id_3, headers_delete)
    delete_user(API_URL, user_id_4, headers_delete)
    delete_user(API_URL, user_id_5, headers_delete)
    delete_user(API_URL, user_id_6, headers_delete)