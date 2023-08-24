from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create and delete group of rules'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, ROLE_USER, name2, login2, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(login2, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    time.sleep(2)
    "pre clean"
    if page.get_by_text("54321").is_visible():
        page.locator(BUTTON_KORZINA).click()
    elif page.get_by_text("12345").is_visible():
        page.locator(BUTTON_KORZINA).click()
    else:
        pass
    '''add new group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("12345")
    page.locator(BUTTON_OTPRAVIT).click()
    '''edit name'''
    page.locator(BUTTON_PENCIL).click()
    page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")
    page.locator(BUTTON_SAVE_EDITED_NAME).click()
    '''check created and edited'''
    expect(page.get_by_text("54321")).to_be_visible(timeout=wait_until_visible)
    '''delete group'''
    page.locator(BUTTON_KORZINA).click()
    '''check deleted'''
    expect(page.get_by_text("54321")).not_to_be_visible(timeout=wait_until_visible)

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)


