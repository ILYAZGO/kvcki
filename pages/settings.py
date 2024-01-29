USERS_LIST = "#react-select-2-input"
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'


BUTTON_NASTROIKI = '[value="settings"]'
BLOCK_LEFT_MENU = ".styles_list__3M7-K"

LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"

BUTTON_ADDRESS_BOOK = '[href*="/address-book"]'
INPUT_ADDRESS_BOOK = '[class*="AddressBookTextArea"]'




def click_settings(page="page: Page"):
    #  go to nastroiki
    page.wait_for_selector(BUTTON_NASTROIKI)
    page.locator(BUTTON_NASTROIKI).click()

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