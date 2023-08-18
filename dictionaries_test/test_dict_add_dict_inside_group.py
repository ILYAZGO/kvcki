from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest
import time


'''Create dict inside group'''

@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(login1, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    '''go to slovari'''
    page.get_by_test_id(BUTTON_SLOVARI).click()
    time.sleep(2)
    '''pre clean'''
    if page.get_by_text("98765").is_visible():

        page.get_by_text("98765").click()

        page.locator(".css-izdlur").click()
        page.get_by_text("Удалить", exact=True).click()
        page.get_by_role("button", name="Удалить").click()
        page.locator(BUTTON_KORZINA).click()
    else:
        pass
    '''create group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("12345")
    page.locator(BUTTON_OTPRAVIT).click()
    '''create dict inside group'''
    page.locator(CLICK_ON_GROUP).click()
    page.get_by_test_id(BUTTON_DOBAVIT_SLOVAR).click()
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
    page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("12345")).not_to_be_visible()


