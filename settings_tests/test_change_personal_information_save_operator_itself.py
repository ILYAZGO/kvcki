from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check impossible changing personal info for operator
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_OPERATOR, PASSWORD, page)

    click_settings(page)

    expect(page.locator(INPUT_EMAIL)).to_be_disabled()
    expect(page.locator(INPUT_PHONE)).to_be_disabled()
    expect(page.locator(INPUT_COMMENT)).to_be_disabled()
    expect(page.locator(INPUT_LOGIN)).to_be_disabled()
    expect(page.locator(INPUT_NAME)).to_be_disabled()
    expect(page.locator(INPUT_NEW_PASSWORD)).to_be_disabled()
    expect(page.locator(INPUT_NEW_PASSWORD_REPEAT)).to_be_disabled()

    expect(page.locator('[class*="typography--variant-body2"]')).to_contain_text("Редактировать персональную информацию может только администратор")

    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)

