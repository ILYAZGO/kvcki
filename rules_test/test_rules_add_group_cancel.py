from playwright.sync_api import Page, expect
from utils.variables import *
import pytest

'''Create and cancel group of rules'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create and cancel adding group'''
    page.get_by_role("link", name="Разметка").click() #razmetka
    page.get_by_test_id("markup_addGroup").click() #Добавить группу
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]").click() #otmena
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible() #надпись Ничего не найдено
    '''create and cancel adding group'''
    page.locator(".styles_addBtn__fyc49").click() #Добавить группу
    page.get_by_test_id("CloseIcon").click() #Крестик
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible() #надпись Ничего не найдено

