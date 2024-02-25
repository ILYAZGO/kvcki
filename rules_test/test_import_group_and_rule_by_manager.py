from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
import pytest
from utils.create_delete_user import create_user, delete_user, give_user_to_manager

'''
Precondition
user  importFrom 
with group 11111 rule 22222 inside
with rule 33333 without group
'''


@pytest.mark.independent
@pytest.mark.rules
def test_example(page: Page) -> None:
    # create user for import
    USER_ID_USER, TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)
    # create manager
    USER_ID_MANAGER, TOKEN_MANAGER, LOGIN_MANAGER = create_user(API_URL, ROLE_MANAGER, PASSWORD)
    # give manager user for import
    give_user_to_manager(API_URL, USER_ID_MANAGER, USER_ID_USER, TOKEN_MANAGER)

    page.goto(URL, timeout=timeout)

    auth(LOGIN_MANAGER, PASSWORD, page)

    '''go to the user to import'''
    page.locator(USERS_LIST).fill(LOGIN_USER)
    page.wait_for_timeout(2000)
    page.get_by_text(LOGIN_USER, exact=True).click()
    page.wait_for_timeout(5000)

    go_to_markup(page)

    '''click Importirovat Pravila'''
    page.wait_for_selector(BUTTON_IMPORTIROVAT_PRAVILA)
    page.locator(BUTTON_IMPORTIROVAT_PRAVILA).click()
    '''type in users list "importFrom" and choose user "importFrom"'''
    page.locator('[class*="simpleSelect"]').locator('[role="combobox"]').fill("importFrom")
    page.wait_for_timeout(1000)
    page.get_by_text("importFrom", exact=True).click()
    page.wait_for_timeout(2000)

    '''click to switch button to import group with rule'''
    page.locator("(//input[@type='checkbox'])[3]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Продолжить").click()
    page.wait_for_timeout(2000)
    '''click to import rule'''
    page.locator("(//input[@type='checkbox'])[6]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="К новым правилам").click()
    page.wait_for_timeout(2000)
    '''check that import successful'''
    expect(page.get_by_text("11111")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1 тег")).to_have_count(count=2, timeout=wait_until_visible)

    '''teardown'''
    page.get_by_text("22222").click()
    page.locator('[width="30"]').click()
    page.get_by_role("button", name="Удалить").click()
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_timeout(700)
    page.get_by_text("33333").click()
    page.locator('[width="30"]').click()
    page.get_by_role("button", name="Удалить").click()
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_timeout(700)

    '''check teardown'''
    expect(page.get_by_text("11111")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).not_to_be_visible(timeout=wait_until_visible)
    page.wait_for_timeout(2600)
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    '''delete manager'''
    delete_user(API_URL, TOKEN_MANAGER, USER_ID_MANAGER)
    '''delete user'''
    delete_user(API_URL, TOKEN_USER, USER_ID_USER)
