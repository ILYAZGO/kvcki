from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.users
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to sotrudniki'''
    page.locator(BUTTON_SOTRUDNIKI).click()
    '''add operator'''
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)
    page.locator(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    ''''''
    page.wait_for_selector(INPUT_NAME)
    page.locator(INPUT_NAME).fill(NEW_OPERATOR_NAME)
    page.locator(INPUT_LOGIN).fill(NEW_OPERATOR_LOGIN)
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(BUTTON_DOBAVIT).click()
    '''go inside operator'''
    page.get_by_text(NEW_OPERATOR_NAME).first.click()
    page.wait_for_timeout(2000)
    '''delete click'''
    page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
    page.wait_for_selector(BUTTON_SOTRUDNIKI_UDALIT)
    ''''''
    page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()

    expect(page.locator(SOTRUDNIK_LOGIN)).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)

