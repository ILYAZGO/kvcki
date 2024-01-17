BUTTON_POLZOVATELI = '[data-testid="userLink"]'
BUTTON_DOBAVIT_POLZOVATELIA = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'
BUTTON_OTMENA = '[data-testid="cancelButton"]'
BUTTON_KRESTIK = '[data-testid="closePopupButton"]'
BUTTON_DOBAVIT = '[data-testid="acceptButton"]'

BUTTON_KORZINA = '[fill="#FF7875"]'                #".styles_menu__tIMGQ svg"
BUTTON_PODTVERDIT = '[data-testid="acceptButton"]' #".FooterButtons_footer__ZUsFp [tabindex='0']:nth-of-type(2)"
BUTTON_NASTROIKI = '[value="settings"]'
BUTTON_SOTRUDNIKI = '[href*="employees"]'
BUTTON_SOTRUDNIKI_UDALIT = "//button[contains(text(),'Удалить')]"
BUTTON_SOTRUDNIKI_KORZINA = ".styles_actions__6AFGJ"

INPUT_POISK = '[name="searchString"]'
INPUT_NAME = '[name="name"]'
INPUT_LOGIN = '[name="login"]'
INPUT_PASSWORD = '[name="password"]'
INPUT_EMAIL = '[name="email"]'
INPUT_COMMENT = '[name="comment"]'
INPUT_QUOTA = '[name="quotaRemindTime"]'

ALERT ="//div/div/div/div/div/div/div/div[2]/div/p"

SOTRUDNIK_LOGIN = "div[role='rowgroup'] div:nth-child(2) div:nth-child(1) div:nth-child(1) div:nth-child(1)"
SOTRUDNIK_NAME = "div[role='rowgroup'] div:nth-child(2) div:nth-child(1) div:nth-child(2) div:nth-child(1)"

SELECT_LANGUAGE = '[data-testid="selectSttLang"]'
SELECT_ENGINE = '[data-testid="selectSttEngine"]'
SELECT_MODEL = '[data-testid="selectSttModel"]'

SELECT_ROLE = '[data-testid="selectRole"]'

FIRST_PAGE_PAGINATION = '[aria-label="1"]'



def go_to_users(page="page: Page"):
    page.wait_for_selector(BUTTON_POLZOVATELI)
    page.locator(BUTTON_POLZOVATELI).click()


def set_user(name, login, password, mail, comment, role, page="page: Page"):
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()  #button create user
    page.wait_for_timeout(1000)
    '''fill required'''
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_timeout(1000)
    page.locator(INPUT_LOGIN).fill(login)
    page.wait_for_timeout(1000)
    page.locator(INPUT_PASSWORD).fill(password)
    page.wait_for_timeout(1000)
    page.locator(INPUT_EMAIL).fill(mail)
    page.wait_for_timeout(1000)
    page.locator(INPUT_COMMENT).fill(comment)
    page.wait_for_timeout(1000)
    page.locator(SELECT_ROLE).locator("svg").click()
    page.wait_for_timeout(1000)
    page.locator(SELECT_ROLE).get_by_text(role, exact=True).click()


def set_stt(language, engine, model, page="page: Page"):

    page.locator(SELECT_LANGUAGE).click()
    page.get_by_text(language, exact=True).click()
    page.wait_for_timeout(500)

    page.locator(SELECT_ENGINE).click()
    page.get_by_text(engine, exact=True).click()
    page.wait_for_timeout(800)

    page.locator(SELECT_MODEL).click()
    page.wait_for_timeout(500)
    page.get_by_text(model, exact=True).click()

def delete_added_user(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).click()
    page.wait_for_selector(BUTTON_PODTVERDIT)
    page.locator(BUTTON_PODTVERDIT).click()