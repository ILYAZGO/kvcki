from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
import pytest
import time

@pytest.mark.users
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''check necessary'''
    expect(page.locator(ALERT)).not_to_be_visible()
    '''fill name'''
    page.locator(INPUT_NAME).fill("someName")
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''check necessary'''
    expect(page.get_by_text("Заполните все обязательные поля")).to_be_visible()
    '''fill login'''
    page.locator(INPUT_LOGIN).fill("1createUserByAdmin")
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''check necessary'''
    expect(page.get_by_text("Заполните все обязательные поля")).to_be_visible()
    '''fill password'''
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''check necessary'''
    expect(page.get_by_text("Заполните все обязательные поля")).not_to_be_visible()
    '''choose role'''
    page.locator(CHOOSE_ROLE).fill("Компания")
    '''press enter'''
    page.keyboard.press("Enter")
    '''press dobavit'''
    page.get_by_test_id(BUTTON_DOBAVIT).click()
    time.sleep(1)
    '''go to profile'''
    page.get_by_text("1createUserByAdmin").click()
    time.sleep(3)
    '''check'''
    expect(page.locator(INPUT_LOGIN)).to_have_value("1createUserByAdmin")
    expect(page.locator(INPUT_NAME)).to_have_value("someName")
    expect(page.get_by_text("Компания")).to_have_count(1)

    '''delete user'''
    page.locator(BUTTON_KORZINA).click()
    page.locator(BUTTON_PODTVERDIT).click()

    expect(page.locator(INPUT_LOGIN)).to_have_value("4adminIM")