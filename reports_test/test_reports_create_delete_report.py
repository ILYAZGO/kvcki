from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
import pytest

'''create , delete report from main report page'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''create report'''
    page.locator(BUTTON_CREATE_REPORT_IN_MENU).click()
    '''switch to all time'''
    page.locator(ALL_TIME).click()



    page.locator(".css-b62m3t-container").get_by_text("Изменить фильтры").click()
    page.locator('[id="Фильтровать по числовым тегам"]').click()
    page.mouse.wheel(delta_x=0, delta_y=10000)
    page.get_by_text("По чеклистам").nth(1).click()
    page.locator(TUPO_CLICK).click()

    page.locator('[autocorrect=off]').nth(0).fill("чеклист")

    page.get_by_text("Второй чеклист (тоже нужен для автотестов, не трогать)", exact=True).click()

    change_grouping_period("По месяцам", page)

    '''change tegs'''
    page.locator(PO_TEGAM_SECOND).nth(0).click()
    page.get_by_text("direction", exact=True).click()
    page.wait_for_timeout(600)
    page.locator(PO_TEGAM_THIRD).nth(1).click()
    page.get_by_text("Выбрать все", exact=True).click()
    '''tupo click'''
    page.locator(TUPO_CLICK).click()
    '''check checkboxes'''
    page.get_by_role("checkbox", checked=False).first.click()
    #page.get_by_role("checkbox", checked=False).first.click()
    # page.get_by_text("Добавить столбец").click()
    '''saving'''
    page.get_by_role("button", name="Сохранить как новый").click()
    page.locator(INPUT_REPORT_NAME).clear()
    page.locator(INPUT_REPORT_NAME).fill("test2345")
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_selector("//h5[contains(text(),'График')]", timeout=wait_until_visible)
    page.get_by_text("Развернуть").click()
    #page.get_by_text("Добавить столбец").click()

    delete_current_report(page)

    expect(page.get_by_text("test2345")).to_have_count(0)
    #page.get_by_role("button", name="Сформировать отчет").click()

