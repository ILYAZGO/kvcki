from playwright.sync_api import Page, expect
from utils.variables import *

'''Create and cancel group of dictionaries'''

def test_example(page: Page) -> None:
    page.goto(URL)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create and cancel adding group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_role("button", name="Словари").click()
    page.locator(".styles_addBtn__fyc49").click() #Добавить группу
    page.get_by_role("button", name="Отмена").click()
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible() #надпись Ничего не найдено
    '''create and cancel adding group'''
    page.locator(".styles_addBtn__fyc49").click() #Добавить группу
    page.get_by_test_id("CloseIcon").click() #Крестик
    '''check canceled'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible() #надпись Ничего не найдено