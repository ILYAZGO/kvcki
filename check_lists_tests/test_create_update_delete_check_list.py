from playwright.sync_api import Page, expect
from utils.variables import *
import pytest

'''Create,delete,update check-list'''

@pytest.mark.check_list
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create check-list'''
    page.locator('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/button[3]/a').click() #razmetka
    page.get_by_test_id("markup_nav_checklists").click() #4ek_list
    page.get_by_test_id("markup_addChecklists").click() #Добавить чек-лист
    page.locator("[name='title']").fill("12345")
    page.locator("[name='questions.0.title']").fill("123456")
    page.locator("[name='questions.0.answers.0.answer']").fill("1234567")
    '''save'''
    page.locator(".MuiButton-contained").click()
    '''check created'''
    expect(page.get_by_text("12345")).to_be_visible()
    expect(page.get_by_text("Чек-лист добавлен")).to_be_visible()
    '''update'''
    page.get_by_text("12345").click()
    page.locator("[name='questions.0.title']").clear()
    page.locator("[name='questions.0.title']").fill("654321")
    '''save'''
    page.locator(".MuiButton-contained").click()
    '''check updated'''
    expect(page.get_by_text("Чек-лист обновлен")).to_be_visible()
    '''delete'''
    page.locator("//*[@id='root']/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div/button").click()
    page.get_by_role("button", name="Удалить").click()
    '''check deleted'''
    expect(page.get_by_text("Чек-лист удален")).to_be_visible()
    expect(page.locator(".styles_noFound__0AI5V")).to_be_visible()