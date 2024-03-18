BUTTON_POLZOVATELI = '[data-testid="userLink"]'
BUTTON_DOBAVIT_POLZOVATELIA = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'
BUTTON_OTMENA = '[data-testid="cancelButton"]'
BUTTON_KRESTIK = '[data-testid="closePopupButton"]'
BUTTON_DOBAVIT = '[data-testid="acceptButton"]'

BUTTON_KORZINA = '[class*="styles_actions"]'
BUTTON_PODTVERDIT = '[data-testid="acceptButton"]'
BUTTON_NASTROIKI = '[value="settings"]'
BUTTON_SOTRUDNIKI = '[href*="settings/employees"]'
BUTTON_SOTRUDNIKI_UDALIT = "//button[contains(text(),'Удалить')]"

INPUT_POISK = '[name="searchString"]'
INPUT_NAME = '[name="name"]'
INPUT_LOGIN = '[name="login"]'
INPUT_PASSWORD = '[name="password"]'
INPUT_EMAIL = '[name="email"]'
INPUT_PHONE = '[name="phoneNumber"]'
INPUT_COMMENT = '[name="comment"]'
INPUT_QUOTA = '[name="quotaRemindTime"]'


USER_LOGIN_IN_LEFT_MENU = '[class*="headerName"]'

SELECT_LANGUAGE = '[data-testid="selectSttLang"]'
SELECT_ENGINE = '[data-testid="selectSttEngine"]'
SELECT_MODEL = '[data-testid="selectSttModel"]'

SELECT_ROLE = '[data-testid="selectRole"]'
SELECT_INDUSTRY = '[data-testid="selectIndustry"]'
SELECT_PARTNER = '[data-testid="selectPartner"]'

FIRST_PAGE_PAGINATION = '[aria-label="1"]'
FIRST_ROW_IN_USERS_LIST = '[aria-rowindex="2"]'


def go_to_users(page="page: Page"):
    page.wait_for_selector(BUTTON_POLZOVATELI)
    page.locator(BUTTON_POLZOVATELI).click()
    page.wait_for_selector(FIRST_ROW_IN_USERS_LIST)

def press_button_add_user(page="page: Page"):
    #page.wait_for_selector(BUTTON_DOBAVIT_POLZOVATELIA)
    page.locator(BUTTON_DOBAVIT_POLZOVATELIA).click()

def press_button_add_employee(page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)
    page.locator(BUTTON_DOBAVIT_SOTRUDNIKA).click()
    page.wait_for_selector(INPUT_NAME)


def set_user(name, login, password, mail, comment, role, page="page: Page"):
    page.wait_for_selector(INPUT_NAME)
    '''fill required'''
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_timeout(200)
    page.locator(INPUT_LOGIN).fill(login)
    page.wait_for_timeout(200)
    page.locator(INPUT_PASSWORD).fill(password)
    page.wait_for_timeout(200)
    page.locator(INPUT_EMAIL).fill(mail)
    page.wait_for_timeout(200)
    page.locator(INPUT_COMMENT).fill(comment)
    page.wait_for_timeout(200)
    page.locator(SELECT_ROLE).locator("svg").click()
    page.wait_for_timeout(200)
    page.locator(SELECT_ROLE).get_by_text(role, exact=True).click()


def set_operator(name, login, password, phone, mail, comment, page="page: Page"):
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_timeout(200)
    page.locator(INPUT_LOGIN).fill(login)
    page.wait_for_timeout(200)
    page.locator(INPUT_PHONE).fill(phone)
    page.wait_for_timeout(200)
    page.locator(INPUT_EMAIL).fill(mail)
    page.wait_for_timeout(200)
    page.locator(INPUT_PASSWORD).fill(password)
    page.wait_for_timeout(200)
    page.locator(INPUT_COMMENT).fill(comment)


def set_industry_and_partner(industry, partner, page="page: Page"):
    page.locator(SELECT_INDUSTRY).locator("svg").click()
    page.wait_for_timeout(800)
    page.locator(SELECT_INDUSTRY).get_by_text(industry, exact=True).click()
    page.wait_for_timeout(800)
    page.locator(SELECT_PARTNER).locator("svg").click()
    page.wait_for_timeout(800)
    page.locator(SELECT_PARTNER).get_by_text(partner, exact=True).click()


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
    #page.wait_for_timeout(300)
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator(BUTTON_KORZINA).click()
    #page.wait_for_timeout(300)
    page.wait_for_selector(BUTTON_PODTVERDIT)
    page.locator(BUTTON_PODTVERDIT).click()


def press_button_add_in_modal(page="page: Page"):
    page.locator(BUTTON_DOBAVIT).click()
    page.wait_for_selector(INPUT_LOGIN)

