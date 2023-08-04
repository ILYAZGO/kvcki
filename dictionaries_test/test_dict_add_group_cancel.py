from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest

'''Create and cancel group of dictionaries'''


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''create and cancel adding group'''
    page.locator(BUTTON_RAZMETKA).click()
    page.get_by_test_id("markup_nav_dicts").click()
    page.locator(".styles_addBtn__fyc49").click()  # Добавить группу
    page.get_by_role("button", name="Отмена").click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible()  # надпись Ничего не найдено
    '''create and cancel adding group'''
    page.locator(".styles_addBtn__fyc49").click()  # Добавить группу
    page.get_by_test_id(BUTTON_KRESTIK).click()
    '''check canceled'''
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible()  # надпись Ничего не найдено
