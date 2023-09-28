from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.calls import *
import pytest

'''Check search by tag for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_period(ALL_TIME, page)

    page.wait_for_selector(INPUT_PO_TEGAM)
    '''input tag'''
    page.locator(INPUT_PO_TEGAM).fill("Другой отдел")
    page.wait_for_timeout(3500)
    page.get_by_text("Другой отдел", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    find_calls(page)

    page.wait_for_selector(FIRST_PAGE_PAGINATION)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 131 из 3130", timeout=wait_until_visible)

    '''add tag'''
    page.locator(INPUT_PO_TEGAM).fill("Обсуждение тарифа")
    page.wait_for_timeout(3500)
    page.get_by_text("Обсуждение тарифа", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    find_calls(page)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 46 из 3130", timeout=wait_until_visible)

    '''click to add condition'''
    page.locator(BUTTON_DOBAVIT_USLOVIE).first.click()

    '''change logic operator'''
    page.locator(CHANGE_LOGIC_OPERATOR).click()
    page.get_by_text("НЕТ ВСЕХ").click()

    '''add tag'''
    page.wait_for_selector(INPUT_PO_TEGAM_NEW)
    page.locator(INPUT_PO_TEGAM_NEW).fill("Новое подключение")
    page.wait_for_timeout(5000)
    page.get_by_text("Новое подключение", exact=True).first.click()
    page.locator(POISK_PO_FRAGMENTAM).click()  # tupo click

    find_calls(page)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 19 из 3130", timeout=wait_until_visible)
