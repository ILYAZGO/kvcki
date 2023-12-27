from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.login import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.login
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    quit_from_profile(page)

    expect(page.locator(BUTTON_VOITI)).to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)




