from playwright.sync_api import Page, expect
from utils.variables import *
from utils.dates import *
from utils.auth import *
from pages.reports import *
import pytest


'''Проверяем кнопки выбора дат'''

@pytest.mark.reports
def test_example(page: Page) -> None:
    page.goto("http://192.168.10.101/feature-dev-895/ru/", timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    '''go to reports'''
    page.locator(BUTTON_OT4ETI).click()
    page.get_by_role("link", name="Создать отчет").click()
    '''switch to all time'''
    page.locator(ALL_TIME).click()
    page.get_by_text("По дням", exact=True).click()
    page.get_by_text("По месяцам", exact=True).click()

    page.locator(".css-19bb58m").click()
    page.get_by_text("direction", exact=True).click()
    page.wait_for_timeout(600)
    page.locator(".css-12ol9ef").click()
    page.get_by_text("Выбрать все", exact=True).click()
    page.locator(".styles_questionTitle__WSOwz").click()
    page.get_by_role("checkbox", checked=False).first.click()
    #page.get_by_text("Добавить столбец").click()
    page.get_by_role("checkbox", checked=False).first.click()
    page.get_by_role("button", name="Сохранить как новый").click()
    page.locator("//html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div/input").clear()
    page.locator("//html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div/input").fill("test2345")
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_selector("//h5[contains(text(),'График')]", timeout=wait_until_visible)
    page.get_by_text("Развернуть").click()
    #page.get_by_text("Добавить столбец").click()


    page.get_by_role("button", name="Удалить шаблон").click()
    page.get_by_role("button", name="Удалить").click()
    expect(page.get_by_text("Сохраненные шаблоны отчетов")).to_have_count(1)
    #page.get_by_role("button", name="Сформировать отчет").click()

