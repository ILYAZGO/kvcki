from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.login import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


@pytest.mark.independent
@pytest.mark.login
def test_example(page: Page) -> None:
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    USER_ID_OPERATOR, TOKEN_OPERATOR, LOGIN_OPERATOR = create_operator(API_URL, USER_ID_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_OPERATOR, PASSWORD, page)

    quit_from_profile(page)

    expect(page.locator(BUTTON_VOITI)).to_be_visible()

    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
    delete_user(API_URL, TOKEN_OPERATOR, USER_ID_OPERATOR)
