from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-1003/ru", timeout = timeout)
    '''login'''
    auth(USER, PASSWORD, page)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to sotrudniki'''
    page.locator(BUTTON_SOTRUDNIKI).click()
    time.sleep(2)

    if page.locator(SOTRUDNIK_LOGIN).is_visible():
        '''go inside operator'''
        page.locator(SOTRUDNIK_LOGIN).click()
        time.sleep(2)
        '''delete click'''
        page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
        ''''''
        page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()
        time.sleep(2)
    else:
        pass

    '''add operator'''
    page.locator(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    ''''''
    page.locator(INPUT_NAME_SOTRUDNIKA).fill("NEW_OPERATOR")
    page.locator(INPUT_LOGIN_SOTRUDNIKA).fill("NEW_OPERATOR_LOGIN")
    page.locator(INPUT_PASSWORD_SOTRUDNIKA).fill("NEW_OPERATOR_PASSWORD")
    page.locator(BUTTON_SOTRUDNIKI_DOBAVIT).click()
    time.sleep(1)

    expect(page.locator(SOTRUDNIK_LOGIN)).to_have_text("NEW_OPERATOR_LOGIN")
    expect(page.locator(SOTRUDNIK_NAME)).to_have_text("NEW_OPERATOR")
    '''go inside operator'''
    page.locator(SOTRUDNIK_LOGIN).click()
    time.sleep(2)
    '''delete click'''
    page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
    ''''''
    page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()

    time.sleep(3)

    expect(page.locator(SOTRUDNIK_LOGIN)).not_to_be_visible()

