from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin can change login for manager
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    go_to_admin_or_manager(LOGIN_MANAGER, page)

    click_settings(page)

    change_login(NEW_LOGIN, page)

    page.reload()
    page.wait_for_selector(INPUT_LOGIN)
    page.wait_for_timeout(300)

    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN)

    #


    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)


