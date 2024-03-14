from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
from utils.create_delete_user import create_user, delete_user, give_user_to_manager
import pytest


@pytest.mark.independent
@pytest.mark.notifications
def test_example(page: Page) -> None:
    # create manager
    USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    # create user for import
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    # give manager user for import
    give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_MANAGER, PASSWORD, page)

    go_to_user(LOGIN_USER, page)

    go_to_notifications_page(page)

    page.locator(BUTTON_IMPORT_RULES).get_by_role("button").click()

    page.wait_for_selector('[data-testid="NotifyRuleCopyMode_search"]')

    page.locator('[aria-haspopup="true"]').nth(2).fill("importFrom")
    page.wait_for_timeout(500)
    page.get_by_text("importFrom", exact=True).click()
    page.wait_for_timeout(800)

    page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(0).click()
    page.wait_for_timeout(800)
    page.get_by_role("button", name="Продолжить").click()
    page.wait_for_timeout(800)
    page.locator('[aria-label="Импортировать"]').locator('[type="checkbox"]').nth(1).click()
    page.wait_for_timeout(800)
    page.get_by_role("button", name="К новым правилам").click()
    page.wait_for_timeout(1600)
    '''check that import successful'''
    expect(page.get_by_text("pochta")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("telega")).to_be_visible(timeout=wait_until_visible)

    # delete first rule
    delete_rule(page)

    expect(page.get_by_text("pochta")).not_to_be_visible(timeout=wait_until_visible)

    # delete second rule
    delete_rule(page)

    expect(page.get_by_text("telega")).not_to_be_visible(timeout=wait_until_visible)

    '''delete manager'''
    delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)
    '''delete user'''
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)