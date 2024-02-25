from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create and delete group of dictionaries'''


@pytest.mark.independent
@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_dicts(page)

    create_group("12345", page)

    '''edit name'''
    page.wait_for_selector(BUTTON_PENCIL)
    page.locator(BUTTON_PENCIL).click()
    page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")
    page.locator(BUTTON_SAVE_EDITED_NAME).get_by_role("button").first.click()
    '''check created and edited'''
    expect(page.get_by_text("54321")).to_be_visible(timeout=wait_until_visible)
    '''delete group'''
    page.locator(BUTTON_KORZINA).click()
    '''check deleted'''
    expect(page.get_by_text("54321")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)