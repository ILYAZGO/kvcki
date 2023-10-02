from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create and cancel group of dictionaries'''


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_dicts(page)

    '''add group'''
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    '''cancel button'''
    page.locator(BUTTON_OTMENA).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено
    '''create and cancel adding group'''
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    '''cancel cross'''
    page.locator(BUTTON_KRESTIK).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)
