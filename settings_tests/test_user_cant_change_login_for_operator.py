from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# changing login disabled for user and operator
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_USER, PASSWORD, page)

    click_settings(page)

    # check disabled for operator

    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)

    go_to_operator_from_table(page)

    expect(page.locator(INPUT_LOGIN)).to_be_disabled()

    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

