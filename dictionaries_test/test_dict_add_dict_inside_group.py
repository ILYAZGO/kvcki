from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest


'''Create dict inside group'''

@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    '''go to slovari'''
    page.locator(BUTTON_SLOVARI).click()
    page.wait_for_selector(BUTTON_DOBAVIT_GRUPPU)
    '''create group'''
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("12345")
    page.locator(BUTTON_OTPRAVIT).click()
    '''create dict inside group'''
    page.locator(CLICK_ON_GROUP).click()
    page.locator(BUTTON_DOBAVIT_SLOVAR).click()
    page.locator(INPUT_NAZVANIE_SLOVAR).fill("98765")
    page.locator(BUTTON_OTPRAVIT).click()
    page.locator(INPUT_SPISOK_SLOV).fill("random_text")
    '''check created dict name'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("98765")
    '''check created dict parent'''
    expect(page.get_by_text("12345").nth(1)).to_have_text("12345") #проверяем что есть родительская группа

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(3000)
    page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("12345")).not_to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)


