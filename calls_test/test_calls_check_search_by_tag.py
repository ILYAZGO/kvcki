from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest

'''Check search by tag for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''za vse vremya'''
    page.wait_for_selector(ALL_TIME)
    page.locator(ALL_TIME).click()
    '''input tag'''
    page.locator(INPUT_PO_TEGAM).fill("Другой отдел")
    page.wait_for_timeout(5000)
    page.get_by_text("Другой отдел", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    page.wait_for_timeout(7000)
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 130 из 3130", timeout=wait_until_visible)
    '''add tag'''
    page.locator(INPUT_PO_TEGAM).fill("Обсуждение тарифа")
    page.wait_for_timeout(5000)
    page.get_by_text("Обсуждение тарифа", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 46 из 3130", timeout=wait_until_visible)
    '''click to add condition'''
    page.locator(BUTTON_DOBAVIT_USLOVIE).click()
    '''change logic operator'''
    page.locator(CHANGE_LOGIC_OPERATOR).click()
    page.get_by_text("НЕТ ВСЕХ").click()
    '''add tag'''
    page.wait_for_selector(INPUT_PO_TEGAM_NEW)
    page.locator(INPUT_PO_TEGAM_NEW).fill("Новое подключение")
    page.wait_for_timeout(5000)
    page.get_by_text("Новое подключение", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click
    '''naity zvonki'''
    page.locator(BUTTON_NAYTI_ZVONKI).click()
    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 19 из 3130", timeout=wait_until_visible)
