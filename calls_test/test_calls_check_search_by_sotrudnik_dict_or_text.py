from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import time
import pytest
'''Check search by sotrudnik dict or text for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''fill client text'''
    page.locator('//*[@id="react-select-8-input"]').fill("адрес")
    time.sleep(3)
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    time.sleep(75)
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 430 из 3130")
    '''choose dict'''
    page.locator('//*[@id="react-select-8-input"]').clear()
    page.locator('//*[@id="react-select-8-input"]').fill("Зо")
    page.get_by_text("Зомбоящик").click()
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()

    time.sleep(100)

    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 488 из 3130")