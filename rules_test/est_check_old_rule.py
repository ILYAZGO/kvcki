from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.markup import *
import pytest

'''https://task.imot.io/browse/DEV-1784   check old rule from ecotelecom'''


@pytest.mark.rules
def test_example(page: Page) -> None:

    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    go_to_markup(page)

    page.wait_for_selector('[href*="/dictionaries?group"]')

    page.locator('[data-testid="test"]').first.click()

    page.wait_for_selector(NAZVANIE_PRAVILA_TEGIROVANIYA)

    '''check canceled'''
    expect(page.locator('[data-testid="fragmentRuleWhoSaid"]')).to_be_visible(timeout=wait_until_visible)  # надпись Ничего не найдено
