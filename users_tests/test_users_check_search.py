from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''wait users list to load'''
    page.wait_for_selector(FIRST_PAGE_PAGINATION)
    '''fill search'''
    page.locator(INPUT_POISK).fill("eco")
    '''check'''
    expect(page.get_by_text("ecotelecom")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1userIM")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)


