from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest
import time

'''Check search by tag for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.locator(ALL_TIME).click()
    '''input tag'''
    page.locator(INPUT_PO_TEGAM).fill("Другой отдел")
    time.sleep(3)
    page.keyboard.press("Enter")
    time.sleep(2)
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    time.sleep(6)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 130 из 3130", timeout=wait_until_visible)
    '''add tag'''
    page.locator(INPUT_PO_TEGAM).fill("Обсуждение тарифа")
    time.sleep(3)
    page.keyboard.press("Enter")
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 46 из 3130", timeout=wait_until_visible)
    '''click to add condition'''
    page.locator(BUTTON_DOBAVIT_USLOVIE).click()
    '''change logic operator'''
    page.locator(CHANGE_LOGIC_OPERATOR).click()
    page.get_by_text("НЕТ ВСЕХ").click()
    '''add tag'''
    page.locator(INPUT_PO_TEGAM_NEW).fill("Новое подключение")
    time.sleep(2)
    page.keyboard.press("Enter")
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено звонков 19 из 3130", timeout=wait_until_visible)
