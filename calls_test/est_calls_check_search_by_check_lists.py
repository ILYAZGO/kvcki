from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest

'''Поиск по чек-листам'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ECOTELECOM, ECOPASS, page)
    choose_period(ALL_TIME, page)
    change_filter("По чеклистам", 1, page)

    # input click
    page.locator("#react-select-16-input").fill("тест")
    # choose filter value
    #page.locator(".css-1lq1yle-menu").get_by_text().click()
    # tupo click
    #page.locator(POISK_PO_FRAGMENTAM).click()



    #choose_filter_value("Бухгалтер", page)
    #find_calls(page)
    '''check'''
    #expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 8 из 3130", timeout=wait_until_visible)
    '''add extra value'''
    #choose_filter_value("Координатор", page)
    #find_calls(page)
    '''check'''
    #expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 362 из 3130", timeout=wait_until_visible)
    #remove_filter_value("Координатор", page)
    #find_calls(page)
    #expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено диалогов 8 из 3130", timeout=wait_until_visible)
