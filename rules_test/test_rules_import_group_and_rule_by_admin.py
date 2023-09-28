from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''
Precondition
user  importFrom 
with group 11111 rule 22222 inside
with rule 33333 without group
'''


@pytest.mark.rules
def test_example(page: Page) -> None:
    '''create admin'''
    USER_ID_ADMIN, BEARER_ADMIN, ACCESS_TOKEN_ADMIN, LOGIN_ADMIN = create_user(API_URL, ROLE_ADMIN, PASSWORD)
    '''create user for import'''
    USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER, LOGIN_USER = create_user(API_URL, ROLE_USER, PASSWORD)

    '''go to page'''
    page.goto(URL, timeout=timeout)
    '''login in admin'''
    auth(LOGIN_ADMIN, PASSWORD, page)
    '''go to the user to import'''
    page.locator(USERS_LIST).fill(LOGIN_USER)
    page.wait_for_timeout(2000)
    page.get_by_text(LOGIN_USER, exact=True).click()
    page.wait_for_timeout(6000)
    '''going to Razmetka and click Importirovat Pravila'''
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_selector(BUTTON_IMPORTIROVAT_PRAVILA)
    page.locator(BUTTON_IMPORTIROVAT_PRAVILA).click()
    '''type in users list "importFrom" and choose user "importFrom"'''
    page.wait_for_selector(INPUT_CHOOSE_USER_FOR_IMPORT)
    page.locator(INPUT_CHOOSE_USER_FOR_IMPORT).get_by_role("combobox").fill("importFrom")
    page.wait_for_timeout(1000)
    page.get_by_text("importFrom", exact=True).click()
    page.wait_for_timeout(2000)
    '''click to switch button to import group with rule'''
    page.locator("(//input[@type='checkbox'])[3]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Продолжить").click()
    page.wait_for_timeout(1000)
    '''click to import rule'''
    page.locator("(//input[@type='checkbox'])[5]").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="К новым правилам").click()
    page.wait_for_timeout(1000)

    '''check that import successful'''
    expect(page.get_by_text("11111")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("1 тег")).to_have_count(count=2, timeout=wait_until_visible)

    '''teardown'''
    page.get_by_text("22222").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_text("33333").click()
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator('[aria-label="Удалить"]').first.click()
    page.wait_for_timeout(1500)
    page.locator('[aria-label="Удалить"]').first.click()

    '''check teardown'''
    expect(page.get_by_text("11111")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("22222")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("33333")).not_to_be_visible(timeout=wait_until_visible)
    expect(page.get_by_text("Неотсортированные")).not_to_be_visible(timeout=wait_until_visible)

    '''delete admin'''
    delete_user(API_URL, USER_ID_ADMIN, BEARER_ADMIN, ACCESS_TOKEN_ADMIN)
    '''delete user'''
    delete_user(API_URL, USER_ID_USER, BEARER_USER, ACCESS_TOKEN_USER)
