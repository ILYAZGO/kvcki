from playwright.sync_api import Page, expect
from utils.variables import *
import pytest

'''Check search by sotrudnik number for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(ADMIN)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''go to user'''
    page.locator("#react-select-2-input").fill("Эк")
    page.get_by_text("Экотелеком", exact=True).click()
    '''go to calls'''
    page.locator('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/button[1]').click()
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    ''''''
    page.locator('//html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').fill("4995055555")
    '''naity zvonki'''
    page.locator('//html/body/div/div/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div[2]/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 670 из 3130")

