from playwright.sync_api import Page, expect
from utils.variables import *
import pytest

'''Create tag in group and outside group'''

@pytest.mark.rules
def test_example(page: Page) -> None:
    fill="QWERTY"
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''create group'''
    page.get_by_role("link", name="Разметка").click()
    page.get_by_test_id("markup_addGroup").click()  # dobavit gruppu
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/div[1]/div[2]/input").fill("99999")  # add name
    page.locator("//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[1]").click()  # otpravit
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div').click() #pereyti na gruppu
    page.get_by_test_id("markup_addTag").click() #dobavit teg
    page.get_by_test_id("markup_newRuleInput").type("88888") #vvesti nazvanie
    page.keyboard.press('Enter') #kostil'
    #page.get_by_test_id("markup_newRuleApply").click() #otpravit
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div/div[2]/div/input')).to_have_value("88888") #check rule
    expect(page.get_by_text("99999").nth(1)).to_have_text("99999") #check parent group

    '''teardown'''
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.locator("//html/body/div/div/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div/div[1]/div[2]/div[2]/div/button").click()
    '''check teardown'''
    expect(page.get_by_text("99999")).not_to_be_visible() #check no parent group








