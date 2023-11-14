from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.notifications
def test_example(page: Page) -> None:
    '''create admin'''
    USER_ID_ADMIN, BEARER_ADMIN, ACCESS_TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    '''create user for import'''
    USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto("http://192.168.10.101/feature-dev-1415/", timeout=timeout)

    '''login in admin'''
    auth(LOGIN_ADMIN, PASSWORD, page)
    '''go to the user to import'''
    page.locator(USERS_LIST).fill(LOGIN_USER)
    page.wait_for_timeout(2000)
    page.get_by_text(LOGIN_USER, exact=True).click()
    page.wait_for_timeout(6000)
    page.locator(BUTTON_OPOVESHENIA).click()
    page.locator(BUTTON_IMPORT_RULES).click()

    page.wait_for_selector('[aria-haspopup="true"]')
    page.locator('[aria-haspopup="true"]').nth(2).fill("importFrom")
    page.wait_for_timeout(1000)
    page.get_by_text("importFrom", exact=True).click()
    page.wait_for_timeout(2000)

    page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(0).click()

    page.get_by_role("button", name="Продолжить").click()

    page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(1).click()

    page.get_by_role("button", name="К новым правилам").click()
    page.wait_for_timeout(2000)
    '''check that import successful'''
    expect(page.get_by_text("pochta")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("telega")).to_be_visible(timeout=wait_until_visible)

    page.locator('[aria-label="Удалить"]').nth(0).click()
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("pochta")).not_to_be_visible(timeout=wait_until_visible)

    page.locator('[aria-label="Удалить"]').nth(0).click()
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(2000)
    expect(page.get_by_text("telega")).not_to_be_visible(timeout=wait_until_visible)

    '''delete admin'''
    delete_user(API_URL, USER_ID_ADMIN, BEARER_ADMIN, ACCESS_TOKEN_ADMIN)
    '''delete user'''
    delete_user(API_URL, USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER)