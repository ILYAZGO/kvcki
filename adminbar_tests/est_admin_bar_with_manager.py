#poka ne rabotaet.vklu4it pozhe

from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import *
import pytest

@pytest.mark.adminbar
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    page.locator("[id='mui-1']").fill(MANAGER)
    page.locator("[id='mui-2']").fill(PASSWORD)
    page.locator("[id='mui-3']").click()
    '''check name have count 2 '''
    expect(page.get_by_text("managerIM")).to_have_count(2)
    '''go to user'''
    page.locator('//*[@id="react-select-2-input"]').fill("userIM")
    page.get_by_text("userIM", exact=True).click()
    '''check name have count 1 and user have count 1'''
    expect(page.get_by_text("managerIM")).to_have_count(1)
    expect(page.get_by_text("userIM")).to_have_count(1)
    '''go back'''
    page.locator('//*[@id="root"]/div/div[1]/button/span').click()
    '''check name have count 2'''
    expect(page.get_by_text("managerIM")).to_have_count(2)

    '''POLZOVATELI!!!!'''