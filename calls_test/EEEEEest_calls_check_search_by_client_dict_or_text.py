from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import pytest
'''Check search by client dict or text for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''fill client text'''
    page.locator('//*[@id="react-select-6-input"]').fill("адрес")
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 14 из 3130")
    '''choose dict'''
    page.locator('//*[@id="react-select-6-input"]').clear()
    #page.locator('//*[@id="react-select-6-input"]').click()
    page.get_by_text("Зомбоящик").click()
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()

    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 14 из 3130")