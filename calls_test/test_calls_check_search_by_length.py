from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import time
import pytest

'''Check search by length for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''fill search by length'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').fill("<10")
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 443 из 3130")

    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').clear()
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').fill(">10")
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 2687 из 3130")

    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').clear()
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div/div[1]/div[2]/input').fill("1711")
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()
    time.sleep(1)
    '''check'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 1 из 3130")