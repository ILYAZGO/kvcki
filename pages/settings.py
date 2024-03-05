USERS_LIST = "#react-select-2-input"
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'

BUTTON_NASTROIKI = '[value="settings"]'
BLOCK_LEFT_MENU = ".styles_list__3M7-K"

LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"

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
    #  go to nastroiki
    page.wait_for_selector(BUTTON_NASTROIKI)
    page.locator(BUTTON_NASTROIKI).click()
    page.wait_for_timeout(1000)
    page.wait_for_selector(INPUT_LOGIN)

def fill_address_book_and_save(Text, page="page: Page"):
    page.locator(BUTTON_ADDRESS_BOOK).click()
    page.wait_for_selector(INPUT_ADDRESS_BOOK)
    page.locator(INPUT_ADDRESS_BOOK).clear()
    page.wait_for_timeout(1000)
    page.locator(INPUT_ADDRESS_BOOK).fill(Text)
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Сохранить").click()
    page.wait_for_timeout(2000)


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
    page.locator('[style="text-transform: none;"]').click()
    page.wait_for_timeout(1000)

def fill_personal_information(name, email, phone, comment , timezone, page="page: Page"):
    page.locator(INPUT_NAME).fill(name)
    page.locator(INPUT_EMAIL).fill(email)
    page.locator(INPUT_PHONE).fill(phone)
    page.locator(INPUT_COMMENT).fill(comment)
    page.locator('[data-testid="selectTimezone"]').locator('[role="combobox"]').click()
    page.get_by_text(timezone).click()
    # save
    page.locator('[style="text-transform: none;"]').click()
    page.wait_for_timeout(500)


def go_to_user(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')

def go_to_admin_or_manager(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_timeout(1500)

