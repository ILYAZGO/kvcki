from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import *
from utils.auth import auth
from pages.reports import *
import pytest


'''Проверяем кнопки выбора дат'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''create report'''
    page.locator('[href*="create"]').click()
    '''switch to all time'''
    page.locator(ALL_TIME).click()
    '''change groupping'''
    page.get_by_text("По дням", exact=True).click()
    page.get_by_text("По месяцам", exact=True).click()
    '''change tegs'''
    page.locator(PO_TEGAM_SECOND).click()
    page.get_by_text("direction", exact=True).click()
    page.wait_for_timeout(600)
    page.locator(PO_TEGAM_THIRD).click()
    page.get_by_text("Выбрать все", exact=True).click()
    '''tupo click'''
    page.locator(TUPO_CLICK).click()
    '''check checkboxes'''
    page.get_by_role("checkbox", checked=False).first.click()
    page.get_by_role("checkbox", checked=False).first.click()
    # page.get_by_text("Добавить столбец").click()
    '''saving'''
    page.get_by_role("button", name="Сохранить как новый").click()
    page.locator(INPUT_REPORT_NAME).clear()
    page.locator(INPUT_REPORT_NAME).fill("test2345")
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_selector("//h5[contains(text(),'График')]", timeout=wait_until_visible)
    page.get_by_text("Развернуть").click()
    #page.get_by_text("Добавить столбец").click()


    page.get_by_role("button", name="Удалить шаблон").click()
    page.get_by_role("button", name="Удалить").click()
    expect(page.get_by_text("Сохраненные отчеты")).to_have_count(1)
    #page.get_by_role("button", name="Сформировать отчет").click()

