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

    '''wait users list to load'''
    page.wait_for_selector('[aria-rowindex="2"]')

    '''fill search'''
    page.locator(INPUT_POISK).fill("ecot")

    '''check'''
    expect(page.get_by_text("ecotelecom")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1userIM")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, TOKEN, USER_ID)


