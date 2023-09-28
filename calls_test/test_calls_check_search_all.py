from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest

'''Check search all calls for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_period(ALL_TIME, page)

    find_calls(page)

    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 3130 из 3130")