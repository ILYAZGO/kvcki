from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.settings import *
from utils.create_delete_user import create_user, delete_user, create_operator
import pytest


# check admin go for managers personal info and check fields industry and partner
@pytest.mark.independent
@pytest.mark.settings
def test_example(page: Page) -> None:

    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_ADMIN, PASSWORD, page)

    go_to_admin_or_manager(LOGIN_MANAGER, page)

    click_settings(page)

    expect(page.locator(SELECT_INDUSTRY)).not_to_be_visible()
    expect(page.locator(SELECT_PARTNER)).not_to_be_visible()

    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)


