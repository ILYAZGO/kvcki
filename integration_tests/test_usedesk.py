from playwright.sync_api import Page, expect
from utils.variables import *
from utils.auth import *
from pages.users import *
from utils.dates import yesterday
from pages.calls import *
from pages.integration import *
import pytest
import time

@pytest.mark.integration
def test_example(page: Page) -> None:
    page.goto(URL, timeout = timeout)
    '''login'''
    auth(ADMIN, PASSWORD, page)
    '''go to polzovateli'''
    page.locator(BUTTON_POLZOVATELI).click()
    page.locator(INPUT_USER_DROPDOWN).fill("usedeskTest")
    time.sleep(2)
    if page.get_by_text("usedeskTest", exact=True).is_visible():
        page.get_by_text("usedeskTest", exact=True).click()
        time.sleep(2)
        '''go to nastroiki'''
        page.locator(BUTTON_NASTROIKI).click()
        time.sleep(3)
        '''delete user'''
        page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
        time.sleep(3)
        page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()
        page.locator(BUTTON_POLZOVATELI).click()
    else:
        pass

    '''button create user'''
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()
    '''fill required'''
    page.locator(INPUT_NAME).fill("usedeskTest")
    page.locator(INPUT_LOGIN).fill("usedesk")
    page.locator(INPUT_PASSWORD).fill(PASSWORD)
    page.locator(CHOOSE_ROLE).fill("Пользователь")
    '''press enter'''
    page.keyboard.press("Enter")
    '''add quota'''
    page.locator(INPUT_QUOTA).fill("100")
    '''press dobavit'''
    page.locator(BUTTON_DOBAVIT).click()
    time.sleep(3)
    '''go to created user'''
    page.locator(INPUT_USER_DROPDOWN).fill("usedeskTest")
    page.get_by_text("usedeskTest", exact=True).click()
    time.sleep(6)
    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    '''go to integracii'''
    page.locator(BUTTON_INTEGRACII_IN_MENU).click()
    '''podklu4it'''
    page.locator(BUTTON_PODKLU4IT).click()
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
    time.sleep(60)
    '''go to zvonki'''
    page.locator(BUTTON_ZVONKI).click()
    time.sleep(3)
    '''press find calls'''
    page.locator(BUTTON_FIND_CALLS).click()
    time.sleep(10)

    expect(page.locator(NAYDENO_ZVONKOV_INTEGRATION)).to_have_text("Найдено звонков 3 из 3")
    time.sleep(3)

    '''go to nastroiki'''
    page.locator(BUTTON_NASTROIKI).click()
    time.sleep(3)
    '''delete user'''
    page.locator(BUTTON_SOTRUDNIKI_KORZINA).click()
    time.sleep(3)
    page.locator(BUTTON_SOTRUDNIKI_UDALIT).click()

    expect(page.locator(LOGIN_IN_LEFT_MENU)).to_have_text("4adminIM")



