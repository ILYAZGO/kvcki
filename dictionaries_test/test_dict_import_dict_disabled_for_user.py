from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_dicts(page)

    '''check '''
    page.wait_for_selector(BUTTON_IMPORTIROVAT_SLOVARI)
    expect(page.locator(BUTTON_IMPORTIROVAT_SLOVARI)).not_to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
