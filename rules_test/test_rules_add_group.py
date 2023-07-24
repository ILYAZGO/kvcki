from playwright.sync_api import Page, expect
from utils.variables import *

'''Create and delete group of rules'''

def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_test_id("markup_addGroup").click()
    page.get_by_role("textbox").fill("12345")
    page.get_by_role("button", name="Отправить").click()
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible()
    '''delete group'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/button').click()
    '''check deleted'''
    expect(page.get_by_text("12345")).not_to_be_visible()

