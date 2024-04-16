USERS_LIST = "#react-select-2-input"

BUTTON_USERS = '[data-testid="userLink"]'
BLOCK_ADMIN_BAR = '[data-testid="adminBar"]'


def go_to_user(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')

def change_lang(current, to, page="page: Page"):
    page.locator('[class*="styles_langHandler"]').get_by_role("button", name=current).click()
    page.wait_for_timeout(300)
    page.get_by_role("option", name=to).click()
    page.wait_for_selector('[class*="Hint_question__title"]')