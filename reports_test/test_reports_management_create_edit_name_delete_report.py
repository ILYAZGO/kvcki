from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.reports import *
from utils.dates import yesterday,today ,first_day_week_ago
from utils.create_delete_user import create_user, delete_user
import pytest


'''Cоздаем отчет и удаляем его через управление отчетами'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(LOGIN, PASSWORD, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()

    page.locator(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV).click()
    page.wait_for_selector(BUTTON_CREATE_REPORT_IN_MANAGEMENT)
    '''create report'''
    page.locator(BUTTON_CREATE_REPORT_IN_MANAGEMENT).click()
    '''switch to all time'''
    page.locator(ALL_TIME).click()
    '''saving'''
    page.get_by_role("button", name="Сохранить как новый").click()
    page.locator(INPUT_REPORT_NAME).clear()
    page.locator(INPUT_REPORT_NAME).fill("auto-test-report")
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(2000)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    '''go to report management'''
    page.wait_for_selector(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV)
    page.locator(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV).click()
    page.wait_for_selector('[aria-label="Изменить название"]')
    '''change name'''
    page.locator('[aria-label="Изменить название"]').click()
    page.wait_for_timeout(500)
    page.locator('[name="reportName"]').clear()
    page.wait_for_timeout(500)
    page.locator('[name="reportName"]').fill("report-test-auto")
    page.wait_for_timeout(500)
    page.locator('[aria-label="Сохранить"]').click()
    page.wait_for_timeout(1000)
    #'''change dates'''
    #page.get_by_text("За все время", exact=True).click()
    #page.get_by_text("Произвольные даты", exact=True).click()
    #'''set beginning date '''
    #page.locator(FIRST_DATE).click()
    #page.get_by_text("Последняя неделя").click()
    #page.locator(FIRST_DATE).fill(yesterday)
    #page.locator(LAST_DATE).click()
    #page.locator(LAST_DATE).fill(today)

    page.locator('[aria-label="Перейти"]').click()

    #expect(page.locator(FIRST_DATE)).to_have_value(first_day_week_ago)
    #expect(page.locator(LAST_DATE)).to_have_value(today)
    '''click OK'''

    page.wait_for_timeout(1500)
    page.locator(BUTTON_OT4ETI).click()
    page.wait_for_selector(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV)
    page.locator(BUTTON_UPRAVLENIE_SPISKOM_OT4ETOV).click()



    '''delete report'''

    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).click()
    page.wait_for_selector(BUTTON_UDALIT)
    page.locator(BUTTON_UDALIT).click()

    page.wait_for_selector(BUTTON_CREATE_REPORT_IN_MANAGEMENT)

    expect(page.get_by_text("report-test-auto")).to_have_count(0)
    expect(page.get_by_text("auto-test-report")).to_have_count(0)


    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)