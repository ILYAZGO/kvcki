from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(USER, PASSWORD, page)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to sotrudniki'''
    page.get_by_role("link", name="Сотрудники").click()
    #page.locator(BUTTON_SOTRUDNIKI).click()
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
    page.get_by_test_id(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    ''''''
    page.locator(INPUT_NAME_SOTRUDNIKA).fill("NEW_OPERATOR")
    page.locator(INPUT_LOGIN_SOTRUDNIKA).fill("NEW_OPERATOR_LOGIN")
    page.locator(INPUT_PASSWORD_SOTRUDNIKA).fill("NEW_OPERATOR_PASSWORD")
    page.locator(BUTTON_DOBAVIT).click()

    expect(page.locator(SOTRUDNIK_LOGIN)).to_have_text("NEW_OPERATOR_LOGIN", timeout=wait_until_visible)
    expect(page.locator(SOTRUDNIK_NAME)).to_have_text("NEW_OPERATOR", timeout=wait_until_visible)
    '''go inside operator'''
    page.locator(SOTRUDNIK_LOGIN).click()
    time.sleep(2)
    '''delete click'''
    page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
    ''''''
    page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()


    expect(page.locator(SOTRUDNIK_LOGIN, timeout=wait_until_visible)).not_to_be_visible()

