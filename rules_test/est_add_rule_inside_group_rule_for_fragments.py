from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest

'''Create rule inside group, check rule for fragments'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_markup(page)

    create_group("99999", page)

    '''click group'''
    page.wait_for_selector(CLICK_NEW_GROUP)
    page.locator(CLICK_NEW_GROUP).click()
    page.wait_for_timeout(2000)

    create_rule("88888", page)

    '''check'''
    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)
    expect(page.locator(NAZVANIE_PRAVILA_TEGIROVANIYA)).to_have_value("88888", timeout=wait_until_visible) #check rule

    # switch "who said?"

    page.get_by_text("Любой сказал").click()
    page.get_by_text("Клиент сказал").click()
    page.get_by_text("Клиент сказал", exact=True).click()
    page.get_by_text("Сотрудник сказал").click()
    page.get_by_text("Сотрудник сказал", exact=True).click()
    page.get_by_text("Любой не сказал").click()
    page.get_by_text("Любой не сказал", exact=True).click()
    page.get_by_text("Клиент не сказал").click()
    page.get_by_text("Клиент не сказал", exact=True).click()
    page.get_by_text("Сотрудник не сказал").click()
    page.get_by_text("Сотрудник не сказал", exact=True).click()
    page.get_by_text("Любой сказал", exact=True ).click()



    delete_group_and_rule_or_dict(page)

    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible(timeout=wait_until_visible) #check no parent group

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)






