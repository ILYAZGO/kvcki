from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.notifications import *
import pytest

@pytest.mark.reports
def test_example(page: Page) -> None:



    page.goto("http://192.168.10.101/feature-dev-1354", timeout=timeout)
    '''login'''
    auth(USER_FOR_IMPORT, PASSWORD, page)

    page.locator(BUTTON_OPOVESHENIA).click()
    #  add new
    page.locator(".styles_addNewRule__zhZVC").get_by_role("button").click()
    #  click to list
    page.locator('[class="css-8mmkcg"]').first.click()
    #  choose email
    page.locator('[class=" css-164zrm5-menu"]').get_by_text("Email", exact=True).click()
    #
    page.locator('[placeholder="Например: Жалоба на сотрудника"]').fill("auto-test-email")

    page.locator('[style="color: rgb(146, 84, 222);"]').click()

    page.locator(".css-woue3h-menu").get_by_text("По тегам", exact=True).nth(1).click()

    page.locator(".styles_title__nLZ-h").click()
    page.locator('[autocorrect=off]').nth(0).fill("22222")
    page.wait_for_timeout(3000)
    page.get_by_text("22222", exact=True).nth(0).click()

    page.locator('[class="styles_textarea__+sldQ"]').fill("someText ")

    page.locator('[aria-label="ID звонка. Пример: 123456789012345678901234"]').click()

    page.locator('[placeholder="Укажите тему письма"]').fill('letterTheme')

    page.locator('[placeholder="example@mail.com"]').fill('mail@.mail.com')

    page.locator('[class="styles_buttonsGroup__aLY1I"]').get_by_role("button").nth(0).click()

    page.wait_for_selector(BUTTON_KORZINA)

    page.locator('[type="checkbox"]').first.click()

    page.locator(BUTTON_KORZINA).click()

    page.locator('[class="styles_buttonsGroup__D0bLG"]').get_by_role("button").nth(1).click()

    expect(page.locator(BUTTON_KORZINA)).not_to_be_visible()
