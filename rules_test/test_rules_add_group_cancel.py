from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create and cancel group of rules'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, name1, login1, PASSWORD)

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
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible) #надпись Ничего не найдено
    '''adding group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    '''cancel add by cross'''
    page.get_by_test_id(BUTTON_KRESTIK).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible) #надпись Ничего не найдено

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)

