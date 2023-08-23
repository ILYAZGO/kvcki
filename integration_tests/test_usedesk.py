from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.dates import yesterday
from pages.calls import *
from pages.integration import *
from utils.create_delete_user import create_user, delete_user
import pytest
import time

@pytest.mark.integration
def test_example(page: Page) -> None:
    USER_ID, BEARER, ACCESS_TOKEN = create_user(API_URL, name_usedesk, login_usedesk, PASSWORD)

    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    time.sleep(2)
    '''go to user'''
    page.locator(INPUT_USER_DROPDOWN).fill("usedeskTest")
    page.get_by_text("usedeskTest", exact=True).click()
    time.sleep(6)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to integracii'''
    page.locator(BUTTON_INTEGRACII_IN_MENU).click()
    '''podklu4it'''
    page.locator(BUTTON_PODKLU4IT).click()
    time.sleep(1)
    '''choose usedesk'''
    page.locator(BUTTON_USEDESK).click()
    time.sleep(2)
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
    time.sleep(2)
    page.locator(BUTTON_OK_IN_DATE).click()
    time.sleep(1)
    page.locator(BUTTON_OK_IN_DATE).click()
    time.sleep(2)
    '''fill limit'''
    page.locator(INPUT_CALLS_LIMIT).fill("3")
    '''sozdat'''
    page.get_by_test_id(BUTTON_SOZDAT).click()
    '''long wait for download'''
    time.sleep(185)
    '''go to zvonki'''
    page.locator(BUTTON_ZVONKI).click()
    time.sleep(4)
    '''go to week'''
    page.locator(WEEK).click()
    time.sleep(2)
    '''press find calls'''
    page.locator(BUTTON_FIND_CALLS).click()

    expect(page.locator(NAYDENO_ZVONKOV_INTEGRATION)).to_have_text("Найдено звонков 3 из 3", timeout=wait_until_visible)
    time.sleep(3)

    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    time.sleep(2)

    page.locator(BUTTON_INTEGRACII_IN_MENU).click()

    page.locator("div[class='styles_button__xgQ1q'] button[type='button']").click()
    time.sleep(1)
    expect(page.locator(BUTTON_PODKLU4IT)).to_be_visible()

    delete_user(API_URL, USER_ID, BEARER, ACCESS_TOKEN)



