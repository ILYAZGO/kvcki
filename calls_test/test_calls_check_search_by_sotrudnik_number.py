from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest


'''Check search by sotrudnik number for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    choose_period(ALL_TIME, page)
    '''add sotrudnik number'''
    page.locator(INPUT_NOMER_SOTRUDNIKA).fill("4995055555")
    find_calls(page)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 670 из 3130", timeout=wait_until_visible)

