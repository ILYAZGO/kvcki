from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
from utils.create_delete_user import create_user, delete_user
import pytest


'''Create dict inside group'''


@pytest.mark.independent
@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)

    auth(LOGIN, PASSWORD, page)

    go_to_dicts(page)

    create_group("12345", page)

    '''create dict inside group'''
    page.locator(CLICK_ON_GROUP).click()

    create_dict("98765", page)

    '''check created dict name'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("98765")

    '''check created dict parent'''
    expect(page.get_by_text("12345").nth(1)).to_have_text("12345") #проверяем что есть родительская группа
    page.wait_for_timeout(300)

    '''rename dict'''
    page.locator(NAZVANIE_SLOVARYA).clear()
    page.locator(NAZVANIE_SLOVARYA).fill("newName")
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(1000)
    '''check name changed'''
    expect(page.locator(NAZVANIE_SLOVARYA)).to_have_value("newName")
    expect(page.locator('[data-testid="test"]')).to_have_text("newName")

    delete_group_and_rule_or_dict(page)

    expect(page.get_by_text("12345")).not_to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)


