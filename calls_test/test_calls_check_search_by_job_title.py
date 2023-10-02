from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest

'''Поиск по Должность'''


@pytest.mark.calls
def test_example(page: Page) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_period(ALL_TIME, page)

    change_filter("Должность", 0, page)

    choose_filter_value("Бухгалтер", page)

    find_calls(page)


    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 8 из 3130", timeout=wait_until_visible)

    '''add extra value'''
    choose_filter_value("Координатор", page)

    find_calls(page)

    '''check'''
    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 362 из 3130", timeout=wait_until_visible)

    remove_filter_value("Координатор", page)

    find_calls(page)

    expect(page.locator(NAYDENO_ZVONKOV)).to_have_text("Найдено коммуникаций 8 из 3130", timeout=wait_until_visible)
