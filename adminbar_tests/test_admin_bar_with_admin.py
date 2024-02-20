from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
import pytest
from utils.create_delete_user import create_user, delete_user


@pytest.mark.adminbar
def test_example(page: Page) -> None:
    #  create admin
    USER_ID_ADMIN, TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    #  create user
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN_ADMIN, PASSWORD, page)
    '''check name have count 2 '''
    expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill(LOGIN_USER)
    page.wait_for_timeout(300)
    page.get_by_text(LOGIN_USER, exact=True).click()
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text(LOGIN_USER, exact=True)).to_have_count(1, timeout=wait_until_visible)
    expect(page.get_by_text("Пользователи")).to_have_count(1, timeout=wait_until_visible)
    '''go back'''
    page.locator('[data-testid="adminBar"]').get_by_role("button").click()
    '''check name have count 2'''
    expect(page.get_by_text(LOGIN_ADMIN)).to_have_count(2, timeout=wait_until_visible)

    #  delete admin
    delete_user(API_URL, TOKEN_ADMIN, USER_ID_ADMIN)
    #  delete user
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)