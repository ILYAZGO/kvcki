from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

'''Create rule in group and outside group'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to razmetka'''
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_selector(BUTTON_DOBAVIT_GRUPPU)
    '''create group'''
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill("99999")
    page.locator(BUTTON_OTPRAVIT).click()
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(2000)
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type("88888")
    page.keyboard.press('Enter') #kostil'
    #page.get_by_test_id("markup_newRuleApply").click() #otpravit
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    '''check'''
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule
    #expect(page.get_by_text("99999").nth(1)).to_have_text("99999", timeout=wait_until_visible) #check parent group
    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.get_by_label("Удалить").first.click()
    #page.locator(BUTTON_KORZINA).click()
    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)






