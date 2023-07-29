from playwright.sync_api import Page, expect
from utils.variables import *

'''Create and delete group of dictionaries'''

def test_example(page: Page) -> None:
    page.goto(URL)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create check-list'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_role("button", name="Чек-листы").click()
    page.locator(".MuiButton-root").click() #Добавить чек-лист
    page.locator("[name='title']").fill("12345")
    page.locator("[name='questions.0.title']").fill("123456")
    page.locator("[name='questions.0.answers.0.answer']").fill("1234567")
    '''scroll and save'''
    #page.mouse.wheel(delta_x=0,delta_y=800)
    page.locator(".MuiButton-contained").click()
    #page.mouse.wheel(delta_x=0, delta_y=-800)
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible()
    '''delete'''
    page.locator("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div/button").click()
    page.get_by_role("button", name="Удалить").click()
    '''check deleted'''
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible()