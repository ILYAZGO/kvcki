from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.markup import *
import pytest
import time

'''Create,delete,update check-list'''

@pytest.mark.check_list
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''create check-list'''
    page.locator(BUTTON_RAZMETKA).click()
    page.get_by_test_id(BUTTON_CHECK_LIST).click()
    page.get_by_test_id(BUTTON_DOBAVIT_CHECK_LIST).click()
    page.locator(INPUT_CHECK_LIST_NAME).fill("12345")
    page.locator("[name='questions.0.title']").fill("123456")
    page.locator("[name='questions.0.answers.0.answer']").fill("1234567")
    '''save'''
    page.locator(".MuiButton-contained").click()
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible()
    #expect(page.get_by_text("Чек-лист добавлен")).to_be_visible()

    '''update'''
    page.get_by_text("12345").click()
    page.locator("[name='questions.0.title']").clear()
    page.locator("[name='questions.0.title']").fill("654321")
    '''save'''
    page.locator(".MuiButton-contained").click()
    #'''check updated'''
    #expect(page.get_by_text("Чек-лист обновлен")).to_be_visible()
    '''delete'''
    page.locator(BUTTON_KORZINA).click()
    page.get_by_role("button", name="Удалить").click()
    time.sleep(4)
    '''check deleted'''
    time.sleep(2)
    #expect(page.get_by_text("Чек-лист удален")).to_be_visible()
    expect(page.locator(NI4EGO_NE_NAYDENO)).to_be_visible()