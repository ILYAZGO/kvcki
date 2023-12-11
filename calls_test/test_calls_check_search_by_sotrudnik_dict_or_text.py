from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest
'''Check search by sotrudnik dict or text for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    '''fill client text'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("адрес")
    page.wait_for_timeout(3000)

    find_calls(page)

    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 431 из 3130", timeout=wait_until_visible)

    '''choose dict'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).clear()
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("Зо")
    page.get_by_text("Зомбоящик").click()

    find_calls(page)

    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 488 из 3130", timeout=wait_until_visible)