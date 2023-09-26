from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_user_to_manager

@pytest.mark.adminbar
def test_example(page: Page) -> None:

    '''create user for import'''
    USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    '''create manager'''
    USER_ID_MANAGER, BEARER_MANAGER, ACCESS_TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    '''give manager user for import'''
    give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, BEARER_MANAGER, ACCESS_TOKEN_MANAGER)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN_MANAGER, PASSWORD, page)
    '''check name have count 2 '''
    expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill(LOGIN_USER)
    page.wait_for_timeout(2000)
    page.get_by_text(LOGIN_USER, exact=True).click()
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text(LOGIN_USER)).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("Пользователи")).to_have_count(1, timeout=wait_until_visible)
    '''go back'''
    page.locator('[data-testid="adminBar"]').get_by_role("button").click()
    '''check name have count 2'''
    expect(page.get_by_text(LOGIN_MANAGER)).to_have_count(2, timeout=wait_until_visible)

    '''delete manager'''
    delete_user(API_URL, USER_ID_MANAGER, BEARER_MANAGER, ACCESS_TOKEN_MANAGER)
    '''delete user'''
    delete_user(API_URL, USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER)


