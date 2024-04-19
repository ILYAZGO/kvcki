from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin go for user personal info and check and change fields industry and partner and go to operator and check
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    # check and change for user
    go_to_user(LOGIN_USER, page)

    click_settings(page)

    expect(page.locator(SELECT_INDUSTRY)).to_be_visible()
    expect(page.locator(SELECT_PARTNER)).to_be_visible()

    change_industry('Ed-tech', page)
    change_partner('managerIM', page)

    press_save(page)

    page.reload()
    page.wait_for_selector(INPUT_LOGIN)
    page.wait_for_timeout(300)

    expect(page.locator(SELECT_INDUSTRY)).to_have_text('Ed-tech')
    expect(page.locator(SELECT_PARTNER)).to_have_text('managerIM')

    # check for operator

    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)

    go_to_operator_from_table(page)

    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

