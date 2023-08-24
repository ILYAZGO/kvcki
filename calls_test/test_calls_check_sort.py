from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import time
import pytest

'''Check sort(4 type) all calls for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator(ALL_TIME).click()
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()

    '''check all calls find, OLD calls first by default'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 3130 из 3130", timeout=wait_until_visible)
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("08.02.22 00:12", timeout=wait_until_visible)

    '''change sort to NEW CALLS'''
    page.locator(CHANGE_SORT).click()
    page.get_by_text("Сначала новые").click()
    time.sleep(2)
    '''check all calls find, NEW CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("16.05.22 18:21", timeout=wait_until_visible)

    '''change sort to SHORT CALLS'''
    page.locator(CHANGE_SORT).click()
    page.get_by_text("Сначала короткие").click()
    time.sleep(3)
    '''check all calls find, SHORT CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 11:41", timeout=wait_until_visible)

    '''change sort to LONG CALLS'''
    page.locator(CHANGE_SORT).click()
    page.get_by_text("Сначала длинные").click()
    time.sleep(3)
    '''check all calls find, LONG CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 18:08", timeout=wait_until_visible)
