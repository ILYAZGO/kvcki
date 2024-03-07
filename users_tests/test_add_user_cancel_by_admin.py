from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_users(page)

    press_button_add_user(page)

    '''cancel by button CANCEL'''
    page.locator(BUTTON_OTMENA).click()

    expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()

    press_button_add_user(page)

    '''cancel by button KRESTIK'''
    page.locator(BUTTON_KRESTIK).click()

    expect(page.locator(INPUT_PASSWORD)).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)