
BUTTON_NASTROIKI = '[value="settings"]'
BLOCK_LEFT_MENU = ".styles_list__3M7-K"

LEFT_MENU_ITEM = "[class='styles_content__MNyQa']"


def click_settings(page="page: Page"):
    #  go to nastroiki
    page.wait_for_selector(BUTTON_NASTROIKI)
    page.locator(BUTTON_NASTROIKI).click()