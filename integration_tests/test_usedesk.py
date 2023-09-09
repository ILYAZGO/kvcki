from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.dates import yesterday
from pages.calls import *
from pages.integration import *
from utils.create_delete_user import create_user, delete_user
import pytest

@pytest.mark.integration
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN, LOGIN = create_user(API_URL, ROLE_USER, PASSWORD)

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
    page.locator(BUTTON_USEDESK).click()
    page.wait_for_timeout(2000)
    '''input token'''
    page.locator(INPUT_API_TOKEN).fill(USEDESK_TOKEN)
    '''save'''
    page.get_by_test_id(BUTTON_SAVE_TOKEN).click()
    '''go to integacii'''
    page.locator(BUTTON_INTEGRACII).click()
    '''play'''
    page.locator(BUTTON_PLAY).click()
    '''set beginning date '''
    page.locator(NA4ALNAYA_DATA).click()
    page.locator(NA4ALNAYA_DATA).fill(yesterday)
    '''click OK'''
    page.wait_for_timeout(2000)
    page.locator(BUTTON_OK_IN_DATE).click()
    page.wait_for_timeout(1000)
    page.locator(BUTTON_OK_IN_DATE).click()
    page.wait_for_timeout(2000)
    '''fill limit'''
    page.locator(INPUT_CALLS_LIMIT).fill("3")
    '''sozdat'''
    page.get_by_test_id(BUTTON_SOZDAT).click()
    '''long wait for download'''
    page.wait_for_timeout(180000)
    '''go to zvonki'''
    page.locator(BUTTON_ZVONKI).click()
    page.wait_for_selector(WEEK)
    '''go to week'''
    page.locator(WEEK).click()
    '''press find calls'''
    page.locator(BUTTON_FIND_CALLS).click()

    expect(page.locator(NAYDENO_ZVONKOV_INTEGRATION)).to_have_text("Найдено звонков 3 из 3", timeout=wait_until_visible)
    page.wait_for_timeout(3000)

    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    page.wait_for_selector(BUTTON_INTEGRACII_IN_MENU)

    page.locator(BUTTON_INTEGRACII_IN_MENU).click()

    page.locator("div[class='styles_button__xgQ1q'] button[type='button']").click()
    page.wait_for_timeout(1000)
    page.get_by_test_id("SettingsCell_deleteBtn").click()
    page.wait_for_timeout(1000)
    expect(page.locator(BUTTON_PODKLU4IT)).to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)



