from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest

'''Check search by length for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    fill_search_length("<10", page)

    press_find_communications(page)
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 443 из 3130", timeout=wait_until_visible)

    fill_search_length(">10", page)

    press_find_communications(page)
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 2687 из 3130", timeout=wait_until_visible)

    fill_search_length("1711", page)

    press_find_communications(page)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 1 из 3130", timeout=wait_until_visible)