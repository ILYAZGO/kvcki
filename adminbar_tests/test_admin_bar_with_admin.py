from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
import time

@pytest.mark.adminbar
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    time.sleep(3)
    '''check name have count 2 '''
    expect(page.get_by_text("adminIM")).to_have_count(2)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill("importFrom")
    page.get_by_text("importFrom", exact=True).click()
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text("adminIM")).to_have_count(1)
    expect(page.get_by_text("importFrom")).to_have_count(1)
    expect(page.get_by_text("Пользователи")).to_have_count(1)
    '''go back'''
    page.locator('//*[@id="root"]/div/div[1]/button/span').click()
    '''check name have count 2'''
    expect(page.get_by_text("adminIM")).to_have_count(2)