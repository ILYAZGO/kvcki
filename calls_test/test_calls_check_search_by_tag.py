from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
import time
'''Check search all calls for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''check'''
    #expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 3130 из 3130")
    ''''''
    page.locator("//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[2]/input").fill("Другой отдел")
    time.sleep(3)
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div/div[1]/div/h6').click()
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    time.sleep(3)
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 131 из 3130")