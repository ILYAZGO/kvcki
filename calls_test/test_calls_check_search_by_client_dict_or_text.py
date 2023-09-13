from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest


'''Check search by client dict or text for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.wait_for_selector(ALL_TIME)
    page.locator(ALL_TIME).click()
    '''fill client text'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).fill("адрес")
    page.wait_for_timeout(3000)
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_timeout(80000)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 152 из 3130", timeout=wait_until_visible)
    '''choose dict'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).clear()
    page.locator(INPUT_SLOVAR_ILI_TEXT_CLIENT).fill("Зо")
    page.get_by_text("Зомбоящик").click()
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_timeout(80000)
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 410 из 3130", timeout=wait_until_visible)