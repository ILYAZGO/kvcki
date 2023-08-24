from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest
'''Check search by length for Ecotelecom'''

@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator(ALL_TIME).click()
    '''fill exact time'''
    page.locator(INPUT_VREMYA_ZVONKA).fill("11:42")
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 5 из 3130", timeout=wait_until_visible)

