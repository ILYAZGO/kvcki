USERS_LIST = "#react-select-2-input"
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'

BUTTON_NASTROIKI = '[value="settings"]'
BUTTON_OPOVESHENIA = '[href*="/notifications"]'
BLOCK_LEFT_MENU = ".styles_list__3M7-K"

LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"

BUTTON_PERSONAL_INFO = '[href*="/profile"]'

BUTTON_RIGHTS = '[href*="/access-rights"]'
BUTTON_SAVE_IN_RIGHTS = '[data-testid="acceptButton"]'
BLOCK_ONE_RIGHT = '[class*="styles_toggleItem_"]'

BUTTON_QUOTAS = '[href*="settings/quotas"]'
INPUT_QUOTA_TIME = '[name="time"]'

BUTTON_ADDRESS_BOOK = '[href*="/address-book"]'
INPUT_ADDRESS_BOOK = '[class*="AddressBookTextArea"]'

BUTTON_EMPLOYEES = '[href*="settings/employees"]'
BUTTON_DOBAVIT_POLZOVATELIA = BUTTON_DOBAVIT_SOTRUDNIKA = '[data-testid="addUserButton"]'

INPUT_LOGIN = '[name="login"]'
INPUT_NAME = '[name="name"]'
INPUT_EMAIL = '[name="email"]'
INPUT_PHONE = '[name="phoneNumber"]'
INPUT_COMMENT = '[name="comment"]'
INPUT_NEW_PASSWORD = '[name="newPassword"]'
INPUT_NEW_PASSWORD_REPEAT = '[name="newPasswordRepeat"]'


def click_settings(page="page: Page"):
    page.wait_for_selector(BUTTON_NASTROIKI)
    page.locator(BUTTON_NASTROIKI).click()
    page.wait_for_timeout(800)
    page.wait_for_selector(INPUT_LOGIN)


def click_notifications(page="page: Page"):
    page.locator(BUTTON_OPOVESHENIA).click()
    page.wait_for_timeout(500)


def click_personal_info(page="page: Page"):
    page.locator(BUTTON_PERSONAL_INFO).click()
    page.wait_for_selector(INPUT_LOGIN)

def click_employees(page="page: Page"):
    page.locator(BUTTON_EMPLOYEES).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SOTRUDNIKA)


def click_rights(page="page: Page"):
    page.locator(BUTTON_RIGHTS).click()
    page.wait_for_selector('[class*="FooterButtons"]')


def click_quota(page="page: Page"):
    page.locator(BUTTON_QUOTAS).click()
    page.wait_for_timeout(800)
    page.wait_for_selector('[class="rs-table-body-info"]')

def click_address_book(page="page: Page"):
    page.locator(BUTTON_ADDRESS_BOOK).click()
    page.wait_for_selector(INPUT_ADDRESS_BOOK)


def fill_quota_time(minutes, page="page: Page"):
    page.locator(INPUT_QUOTA_TIME).clear()
    page.locator(INPUT_QUOTA_TIME).fill(minutes)

def press_add_in_quotas(page="page: Page"):
    page.get_by_role("button", name="Добавить", exact=True).click()

def fill_address_book(Text, page="page: Page"):
    page.locator(INPUT_ADDRESS_BOOK).clear()
    page.wait_for_timeout(800)
    page.locator(INPUT_ADDRESS_BOOK).fill(Text)
    page.wait_for_timeout(800)


def choose_preiod_date(firstDate, lastDate, page="page: Page"):
    page.locator(FIRST_DATE).click()
    page.locator(FIRST_DATE).fill(firstDate)
    page.wait_for_timeout(500)
    page.locator(LAST_DATE).click()
    page.locator(LAST_DATE).fill(lastDate)
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")

def change_login(login, page="page: Page"):
    page.wait_for_selector(INPUT_LOGIN)
    page.locator(INPUT_LOGIN).clear()
    page.locator(INPUT_LOGIN).fill(login)


def fill_personal_information(name, email, phone, comment , timezone, page="page: Page"):
    page.locator(INPUT_NAME).fill(name)
    page.wait_for_timeout(300)
    page.locator(INPUT_EMAIL).fill(email)
    page.wait_for_timeout(300)
    page.locator(INPUT_PHONE).fill(phone)
    page.wait_for_timeout(300)
    page.locator(INPUT_COMMENT).fill(comment)
    page.wait_for_timeout(200)
    page.locator('[data-testid="selectTimezone"]').locator('[role="combobox"]').click()
    page.get_by_text(timezone).click()
    page.wait_for_timeout(1000)


def go_to_user(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')

def go_to_operator_from_table(page="page: Page"):
    page.wait_for_selector('[role="gridcell"]')
    page.locator('[aria-rowindex="2"]').locator('[class="rs-table-cell rs-table-cell-first"]').click()
    page.wait_for_timeout(500)
    page.wait_for_selector(INPUT_LOGIN)

def go_to_admin_or_manager(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_timeout(1500)

def press_save(page="page: Page"):
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(800)

def press_save_in_rights(page="page: Page"):
    page.locator('[data-testid="acceptButton"]').click()
    page.wait_for_timeout(400)

def click_all_checkboxes_on_page(page="page: Page"):
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    # Выполняем клик на каждом чекбоксе
    for checkbox in checkboxes:
        if not checkbox.is_checked():
            checkbox.click()

def all_checkboxes_to_be_checked(page="page: Page"):
    # Находим все чекбоксы на странице
    checkboxes = page.query_selector_all('input[type="checkbox"]')
    # Проверяем состояние каждого чекбокса
    all_checked = all(checkbox.is_checked() for checkbox in checkboxes)
    return all_checked