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
    page.wait_for_selector(ALL_TIME)
    page.locator(ALL_TIME).click()
    '''fill search by length'''
    page.locator(INPUT_DLITELNOST_ZVONKA).fill("<10")
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 443 из 3130", timeout=wait_until_visible)

    page.locator(INPUT_DLITELNOST_ZVONKA).clear()
    page.locator(INPUT_DLITELNOST_ZVONKA).fill(">10")
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 2687 из 3130", timeout=wait_until_visible)

    page.locator(INPUT_DLITELNOST_ZVONKA).clear()
    page.locator(INPUT_DLITELNOST_ZVONKA).fill("1711")
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_timeout(4000)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 1 из 3130", timeout=wait_until_visible)