from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest
'''Check search by length for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_period(ALL_TIME, page)

    '''fill exact time'''
    page.locator(INPUT_VREMYA_ZVONKA).fill("11:42")

    find_calls(page)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 5 из 3130", timeout=wait_until_visible)

