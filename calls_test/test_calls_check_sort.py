from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest

'''Check sort(4 type) all calls for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_period(ALL_TIME, page)

    find_calls(page)

    '''check all calls find, OLD calls first by default'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 3130 из 3130", timeout=wait_until_visible)
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("08.02.22 00:12", timeout=wait_until_visible)

    change_sort("Сначала новые", page)

    '''check all calls find, NEW CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("16.05.22 18:21", timeout=wait_until_visible)

    change_sort("Сначала короткие", page)

    '''check all calls find, SHORT CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 11:41", timeout=wait_until_visible)

    change_sort("Сначала длинные", page)

    '''check all calls find, LONG CALLS first'''
    expect(page.locator(CALL_DATE_AND_TIME)).to_have_text("09.02.22 18:08", timeout=wait_until_visible)
