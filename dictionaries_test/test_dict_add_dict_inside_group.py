from playwright.sync_api import Page, expect
from utils.variables import *


'''Create dict inside group'''

def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_test_id("markup_nav_dicts").click()
    page.locator(".styles_addBtn__fyc49").click() #Добавить группу
    page.get_by_role("textbox").fill("12345")
    page.get_by_role("button", name="Отправить").click()
    '''create dict inside group'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div').click()
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/button').click()
    page.locator('//html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[2]/input').fill("98765")
    page.get_by_role('button', name="Отправить").click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[2]/div/div/div/div[3]/div[2]/textarea").fill("random_text")
    '''check created dict name'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/div/input')).to_have_value("98765")
    '''check created dict parent'''
    expect(page.get_by_text("12345").nth(1)).to_have_text("12345") #проверяем что есть родительская группа

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/button").click()
    '''check teardown'''
    expect(page.get_by_text("12345")).not_to_be_visible()


