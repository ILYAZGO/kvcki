from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import auth
from pages.users import *
from utils.dates import first_day_week_ago
from pages.calls import *
from pages.integration import *
from utils.create_delete_user import create_user, delete_user
import pytest


@pytest.mark.independent
@pytest.mark.integration
def test_example(page: Page) -> None:
    USER_ID, TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

    page.goto(URL, timeout=timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.wait_for_timeout(2000)
    '''go to user'''
    page.locator(INPUT_USER_DROPDOWN).fill(LOGIN)
    page.get_by_text(text=LOGIN, exact=True).click()
    page.wait_for_timeout(6000)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to integracii'''
    page.locator(BUTTON_INTEGRACII_IN_MENU).click(timeout=wait_until_visible)
    '''podklu4it'''
    page.locator(BUTTON_PODKLU4IT).click()
    page.wait_for_timeout(1000)
    '''choose usedesk'''
    page.locator(".styles_body__L76ER", has_text="usedesk").get_by_role("button").click()

    input_save_api_token(page)

    '''go to integacii'''
    page.locator(BUTTON_INTEGRACII).click()
    '''play'''
    page.locator(BUTTON_PLAY).click()

    set_date(first_day_week_ago, page)

    set_calls_limit("3", page)

    '''sozdat'''
    page.locator(BUTTON_SOZDAT).click()
    '''long wait for download'''
    page.wait_for_timeout(240000)

    page.reload()
    page.wait_for_selector('[class*=headerRow]')
    expect(page.locator('[role="rowgroup"]').locator('[role="cell"]').nth(4)).to_have_text('3')



    #'''go to zvonki'''
    #page.locator(BUTTON_ZVONKI).click()
    #page.wait_for_selector(WEEK)
    #'''go to week'''
    #page.locator(WEEK).click()
    #'''press find calls'''
    #page.locator(BUTTON_FIND_CALLS).click()

    #expect(page.locator(NAYDENO_ZVONKOV_INTEGRATION)).to_have_text("Найдено коммуникаций 3 из 3", timeout=wait_until_visible)
    #page.wait_for_timeout(3000)

    #page.locator(BUTTON_NASTROIKI).click()

    #page.wait_for_selector(BUTTON_INTEGRACII_IN_MENU)


    page.locator(BUTTON_INTEGRACII_IN_MENU).click()

    delete_integration(page)

    expect(page.locator(BUTTON_PODKLU4IT)).to_be_visible()

    delete_user(API_URL, TOKEN, USER_ID)



