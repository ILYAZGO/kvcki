from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest

'''Create and cancel group of dictionaries'''


@pytest.mark.dictionaries
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''create and cancel adding group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_test_id("markup_nav_dicts").click()
    page.locator(".styles_addBtn__fyc49").click()  # Добавить группу
    page.get_by_role("button", name="Отмена").click()
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible()  # надпись Ничего не найдено
    '''create and cancel adding group'''
    page.locator(".styles_addBtn__fyc49").click()  # Добавить группу
    page.get_by_test_id("CloseIcon").click()  # Крестик
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible()  # надпись Ничего не найдено
