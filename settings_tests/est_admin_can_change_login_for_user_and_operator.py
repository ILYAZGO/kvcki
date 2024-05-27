from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin can change login for user and operator
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    NEW_OPERATOR_NAME = NEW_OPERATOR_LOGIN = f"auto_test_operator_{datetime.now().strftime('%m%d%H%M')}_{datetime.now().microsecond}"

    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    # change login for user
    go_to_user(LOGIN_USER, page)

    click_settings(page)

    change_login(CHANGED_LOGIN2, page)

    press_save(page)

    page.reload()
    page.wait_for_selector(INPUT_LOGIN)
    page.wait_for_timeout(300)

    expect(page.locator(INPUT_LOGIN)).to_have_value(CHANGED_LOGIN2)

    # change for operator

    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)

    go_to_operator_from_table(page)

    change_login(NEW_OPERATOR_LOGIN, page)

    press_save(page)

    page.reload()
    page.wait_for_selector(INPUT_LOGIN)
    page.wait_for_timeout(300)

    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_OPERATOR_LOGIN)

    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

