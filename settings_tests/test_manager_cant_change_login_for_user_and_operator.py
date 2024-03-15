from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator, give_user_to_manager
import pytest


# changing login disabled for user and operator
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_MANAGER, PASSWORD, page)

    # check disabled for user
    go_to_user(LOGIN_USER, page)

    click_settings(page)

    expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    # check disabled for operator

    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)

    go_to_operator_from_table(page)

    expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

