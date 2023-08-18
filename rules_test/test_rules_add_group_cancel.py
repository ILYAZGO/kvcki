from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest
import time

'''Create and cancel group of rules'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(login1, PASSWORD, page)
    time.sleep(2)
    '''adding group'''
    page.locator(BUTTON_RAZMETKA).click()
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    '''cancel add'''
    page.locator(BUTTON_OTMENA).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible() #надпись Ничего не найдено
    '''adding group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    '''cancel add by cross'''
    page.get_by_test_id(BUTTON_KRESTIK).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible() #надпись Ничего не найдено

