from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule in group and outside group'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''create rule inside group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(2000)
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type("88888")
    page.keyboard.press('Enter') #kostil'
    #page.get_by_test_id("markup_newRuleApply").click() #otpravit

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule
    #expect(page.get_by_text("99999").nth(1)).to_have_text("99999", timeout=wait_until_visible) #check parent group

    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)






