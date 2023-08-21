from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
import time

@pytest.mark.adminbar
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(MANAGER, PASSWORD, page)
    time.sleep(5)
    '''check name have count 2 '''
    expect(page.get_by_text("managerIM")).to_have_count(2)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill("userIM")
    time.sleep(2)
    page.get_by_text("userIM", exact=True).click()
    time.sleep(3)
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text("managerIM")).to_have_count(1)
    expect(page.get_by_text("userIM")).to_have_count(1)
    expect(page.get_by_text("Пользователи")).to_have_count(1)
    '''go back'''
    page.locator("[class*=simpleButton_root]").click()
    time.sleep(10)
    '''check name have count 2'''
    expect(page.get_by_text("managerIM")).to_have_count(2)
