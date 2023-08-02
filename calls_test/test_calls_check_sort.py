from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
import time
import pytest
'''Check sort(4 type) all calls for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''naity zvonki'''
    page.locator('//html/body/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/button').click()

    '''check all calls find, OLD calls first by default'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/p')).to_have_text("Найдено звонков 3130 из 3130")
    expect(page.locator('//html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/p')).to_have_text("08.02.22 00:12")

    '''change sort to NEW CALLS'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div').click()
    page.get_by_text("Сначала новые").click()
    '''check all calls find, NEW CALLS first'''
    expect(page.locator('//html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/p')).to_have_text("16.05.22 18:21")

    '''change sort to SHORT CALLS'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div').click()
    page.get_by_text("Сначала короткие").click()
    time.sleep(3)
    '''check all calls find, SHORT CALLS first'''
    expect(page.locator('//html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/p')).to_have_text("09.02.22 11:41")

    '''change sort to LONG CALLS'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[1]/div').click()
    page.get_by_text("Сначала длинные").click()
    '''check all calls find, LONG CALLS first'''
    expect(page.locator('//html/body/div/div/div/div[2]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/p')).to_have_text("09.02.22 18:08")