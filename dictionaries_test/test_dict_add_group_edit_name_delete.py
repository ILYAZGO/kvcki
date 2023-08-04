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
    page.get_by_test_id("markup_nav_dicts").click() #go to slovari
    page.get_by_test_id("markup_addGroup").click() #add group
    page.get_by_role("textbox").fill("12345")
    page.locator('//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[1]').click()
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