
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