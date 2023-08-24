from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import time
import pytest
'''Check search by sotrudnik dict or text for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator(ALL_TIME).click()
    '''fill client text'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("адрес")
    time.sleep(3)
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    time.sleep(80)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 431 из 3130", timeout=wait_until_visible)
    '''choose dict'''
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).clear()
    page.locator(INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK).fill("Зо")
    page.get_by_text("Зомбоящик").click()
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    time.sleep(80)
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 488 из 3130", timeout=wait_until_visible)