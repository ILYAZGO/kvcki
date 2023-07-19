from playwright.sync_api import Page, expect
from utils.variables import *

'''Create tag in group and outside group'''

def test_example(page: Page) -> None:
    fill="QWERTY"
    page.goto(URL)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_role("button", name="Добавить группу").click()
    page.get_by_role("textbox").fill("12345")
    page.get_by_role("button", name="Отправить").click()
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div').click()
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/button').click()
    enab = page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div/div[2]/input").is_enabled()
    print(enab)


    #waiting for element to be visible, enabled and editable element.tagName.toUpperCase is not a function

    #page.locator('[name="tagName"]').
    #page.get_by_role("button", name="Отправить").click()
    '''check created'''
    #expect(page.get_by_text("12345")).to_be_visible()
    '''delete group'''
    #page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/button').click()
    '''check deleted'''
    #expect(page.get_by_text("12345")).not_to_be_visible()

