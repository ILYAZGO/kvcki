from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check how many items in left menu for role
@pytest.mark.left_menu
def test_example(page: Page) -> None:
    USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, BEARER_OPERATOR, ACCESS_TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL,USER_ID_USER,PASSWORD)


    page.goto(URL, timeout=timeout)

    auth(LOGIN_OPERATOR, PASSWORD, page)

    click_settings(page)

    expect(page.locator(BLOCK_LEFT_MENU)).to_contain_text(['Персональная информация'])
    expect(page.locator(LEFT_MENU_ITEM)).to_have_count(1)

    delete_user(API_URL, USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER)
    delete_user(API_URL, USER_ID_OPERATOR, BEARER_OPERATOR, ACCESS_TOKEN_OPERATOR)

