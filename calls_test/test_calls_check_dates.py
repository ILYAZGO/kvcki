from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from utils.dates import *
from pages.calls import *
import pytest

'''Проверяем кнопки выбора дат'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''check begin and end dates in view. today by default'''
    expect(page.locator(FIRST_DATE)).to_have_value(today)
    expect(page.locator(LAST_DATE)).to_have_value(today)
    '''switch to yesterday'''
    page.locator(YESTERDAY ).click()
    '''check begin and end dates in view. '''
    expect(page.locator(FIRST_DATE)).to_have_value(yesterday)
    expect(page.locator(LAST_DATE)).to_have_value(yesterday)
    '''switch to week'''
    page.locator(WEEK).click()
    ''''''
    expect(page.locator(FIRST_DATE)).to_have_value(first_day_week_ago)
    expect(page.locator(LAST_DATE)).to_have_value(today)
    '''switch to month'''
    page.locator(MONTH).click()
    ''''''
    expect(page.locator(FIRST_DATE)).to_have_value(first_day_month_ago)
    expect(page.locator(LAST_DATE)).to_have_value(today)
    '''switch to year'''
    page.locator(YEAR).click()
    ''''''
    expect(page.locator(FIRST_DATE)).to_have_value(first_day_year_ago)
    expect(page.locator(LAST_DATE)).to_have_value(today)
    '''switch to all time'''
    page.locator(ALL_TIME).click()
    '''check begin and end dates is disabled '''
    expect(page.locator(FIRST_DATE)).to_be_disabled()
    expect(page.locator(LAST_DATE)).to_be_disabled()



