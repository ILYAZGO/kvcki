from playwright.sync_api import Page, expect, BrowserContext
from utils.variables import *
from utils.auth import auth
from pages.calls import *
import pytest
'''Check search by ID for Ecotelecom'''


@pytest.mark.calls
def test_example(page: Page, context: BrowserContext) -> None:
    page.goto(URL, timeout=timeout)

    auth(ECOTELECOM, ECOPASS, page)

    choose_preiod_date("01/01/2022", "31/12/2022", page)

    '''fill exact id'''
    page.wait_for_selector(INPUT_ID)
    page.locator(INPUT_ID).fill("1644268426.90181")

    press_find_communications(page)
    # open
    with context.expect_page() as new_tab_event:
        page.locator('[id="62050bec113619d283d9d584"]').get_by_role("button").nth(1).click()
        new_tab=new_tab_event.value

    expect(new_tab.locator(AUDIO_PLAYER)).to_have_count(1)
    expect(new_tab.locator('[id="accordionSummary"]')).to_have_count(1)
    expect(new_tab.locator('[id="62050BEC113619D283D9D584"]')).to_have_count(1)
    expect(new_tab.locator('[class*="ClientBlock_employeePhone"]')).to_have_text("79161489993")
    expect(new_tab.locator('[class*="ClientBlock_employeeDuration"]')).to_have_text("00:00:42")
    expect(new_tab.locator('[aria-label="Применение GPT правила"]')).to_have_count(1)
    expect(new_tab.locator('[aria-label="Перетегировать"]')).to_have_count(1)
    expect(new_tab.locator('[aria-label="Скачать"]')).to_have_count(1)
    expect(new_tab.locator('[aria-label="Excel экспорт"]')).to_have_count(1)
    expect(new_tab.locator('[aria-label="Скопировать публичную ссылку"]')).to_have_count(1)
    expect(new_tab.locator('[class*="styles_withAllComments_"]')).to_have_count(1)
    expect(new_tab.get_by_text("Добавить комментарий")).to_have_count(1)
