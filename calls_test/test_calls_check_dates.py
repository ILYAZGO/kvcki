from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from utils.dates import *
import pytest

'''Проверяем кнопки выбора дат'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''check begin and end dates in view. today by default'''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_have_value(today)
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_have_value(today)
    '''switch to yesterday'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[1]').click()
    '''check begin and end dates in view. '''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_have_value(yesterday)
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_have_value(yesterday)
    '''switch to week'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[3]').click()
    ''''''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_have_value(first_day_week_ago)
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_have_value(today)
    '''switch to month'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[4]').click()
    ''''''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_have_value(first_day_month_ago)
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_have_value(today)
    '''switch to year'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[5]').click()
    ''''''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_have_value(first_day_year_ago)
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_have_value(today)
    '''switch to all time'''
    page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/button[6]').click()
    '''check begin and end dates is disabled '''
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input')).to_be_disabled()
    expect(page.locator('//*[@id="root"]/div/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div/div[3]/input')).to_be_disabled()



