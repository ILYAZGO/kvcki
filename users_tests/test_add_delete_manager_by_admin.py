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

    go_to_users(wait_until_visible, page)

    set_user(NEW_NAME,
             NEW_LOGIN,
             PASSWORD,
             EMAIL2,
             "someComment",
             "Интегратор",
             page)

    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(INPUT_LOGIN, timeout=wait_until_visible)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value(NEW_LOGIN, timeout=wait_until_visible)
    expect(page.locator(INPUT_NAME)).to_have_value(NEW_NAME, timeout=wait_until_visible)
    expect(page.locator(INPUT_EMAIL)).to_have_value(EMAIL2, timeout=wait_until_visible)
    expect(page.locator('[data-testid="selectRole"]').get_by_text("Интегратор")).to_have_count(1, timeout=wait_until_visible)

    delete_added_user(page)

    expect(page.locator(INPUT_LOGIN)).to_have_value(LOGIN, timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)