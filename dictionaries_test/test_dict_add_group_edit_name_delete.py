from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest

'''Create and delete group of dictionaries'''

@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''create group'''
    page.locator(BUTTON_RAZMETKA).click()
    '''go to slovari'''
    page.get_by_test_id(BUTTON_SLOVARI).click()

    "pre clean"
    if page.get_by_text("54321").is_visible():
        page.locator(BUTTON_KORZINA).click()
    elif page.get_by_text("12345").is_visible():
        page.locator(BUTTON_KORZINA).click()
    else:
        pass

    '''add group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    page.get_by_role("textbox").fill("12345")
    page.locator(BUTTON_OTPRAVIT).click()
    '''edit name'''
    page.locator(BUTTON_PENCIL).click()  # pencil
    page.locator(INPUT_EDIT_GROUP_NAME).fill("54321")  # fill
    page.locator(BUTTON_SAVE_EDITED_NAME).click()  # save
    '''check created and edited'''
    expect(page.get_by_text("54321")).to_be_visible()
    '''delete group'''
    page.locator(BUTTON_KORZINA).click()
    '''check deleted'''
    expect(page.get_by_text("54321")).not_to_be_visible()