from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest
'''Check search by sotrudnik dict or text for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.wait_for_selector(ALL_TIME, timeout=wait_until_visible)
    page.locator(ALL_TIME).click()
    '''fill client text'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("адрес")
    page.wait_for_timeout(3000)
    '''naity zvonki'''
    page.get_by_role("button", name="Найти диалоги").click()
    #page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 431 из 3130", timeout=wait_until_visible)
    '''choose dict'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).clear()
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("Зо")
    page.get_by_text("Зомбоящик").click()
    '''naity zvonki'''
    page.get_by_role("button", name="Найти диалоги").click()
    #page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 488 из 3130", timeout=wait_until_visible)