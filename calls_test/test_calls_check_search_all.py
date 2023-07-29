from playwright.sync_api import Page, expect
from utils.variables import *
import pytest
'''Check search all calls for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ECOTELECOM)
    page.locator("[id='mui-2']").fill(ECOPASS)
    page.locator("[id='mui-3']").click()
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 3130 из 3130")