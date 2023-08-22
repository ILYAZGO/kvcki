from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create tag in group and outside group'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, name3, login3, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(login3, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()

    '''create group'''
    page.get_by_test_id(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("99999")
    page.locator(BUTTON_OTPRAVIT).click()
    page.locator(CLICK_NEW_GROUP).click()
    page.get_by_test_id(BUTTON_DOBAVIT_TEG).click()
    page.get_by_test_id(INPUT_NAZVANIE_TEGA).type("88888")
    page.keyboard.press('Enter') #kostil'
    #page.get_by_test_id("markup_newRuleApply").click() #otpravit

    '''check'''
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888") #check rule
    expect(page.get_by_text("99999").nth(1)).to_have_text("99999") #check parent group

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    time.sleep(2)
    page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible() #check no parent group

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)






