from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    #USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, ROLE_USER, name10, login10, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(USER, PASSWORD, page)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to sotrudniki'''
    page.get_by_role("link", name="Сотрудники").click()
    #page.locator(BUTTON_SOTRUDNIKI).click()
    page.wait_for_timeout(3000)

    '''add operator'''
    page.get_by_test_id(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    ''''''
    page.locator(INPUT_NAME_SOTRUDNIKA).fill(NEW_OPERATOR_NAME)
    page.locator(INPUT_LOGIN_SOTRUDNIKA).fill(NEW_OPERATOR_LOGIN)
    page.locator(INPUT_PASSWORD_SOTRUDNIKA).fill(PASSWORD)
    page.get_by_test_id(BUTTON_DOBAVIT).click()
    expect(page.locator(SOTRUDNIK_LOGIN)).to_have_text(NEW_OPERATOR_LOGIN, timeout=wait_until_visible)
    expect(page.locator(SOTRUDNIK_NAME)).to_have_text(NEW_OPERATOR_NAME, timeout=wait_until_visible)
    '''go inside operator'''
    page.locator(SOTRUDNIK_LOGIN).click()
    page.wait_for_timeout(2000)
    '''delete click'''
    page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
    page.wait_for_timeout(2000)
    ''''''
    page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()
    page.wait_for_selector(SOTRUDNIK_LOGIN)

    expect(page.locator(SOTRUDNIK_LOGIN)).not_to_be_visible(timeout=wait_until_visible)

    #delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)

