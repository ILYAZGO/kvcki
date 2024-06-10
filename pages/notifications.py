BUTTON_OPOVESHENIA = '[href*="/notifications"]'
USERS_LIST = "#react-select-2-input"

BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_IMPORT_RULES = '[class*="styles_importTagRules"]'

INPUT_NOTIFICATION_NAME = '[name="notifyTitle"]'

INPUT_LETTER_THEME = '[name="emailSubj"]'
INPUT_EMAIL = '[placeholder="example@mail.com"]'
INPUT_HEADERS = '[placeholder="Можно проставить авторизацию и content-type"]'
INPUT_URL = '[name="apiUrl"]'
INPUT_COMMENT = '[class="styles_textarea__+sldQ"]'

BLOCK_RULE_MAIN_AREA = '[class*="mainArea"]'
BLOCK_RULES_LIST = '[class*="sidebar"]'
BlOCK_API = '[class*="InputWithSelect_root"]'
BLOCK_ADD_NEW_RULE = '[class*="styles_addNewRule_"]'


def go_to_notifications_page(page="page: Page"):
    page.locator(BUTTON_OPOVESHENIA).click()
    page.wait_for_selector(BLOCK_ADD_NEW_RULE)


def set_notification_name(notificationName, page="page: Page"):
    page.locator(INPUT_NOTIFICATION_NAME).fill(notificationName)


def add_filter(filterType, filterName, elementNumber, page="page: Page"):
    #  dobavit filtr
    page.locator('[style="color: rgb(146, 84, 222);"]').click()
    #  choose po tegam
    page.locator(".css-woue3h-menu").get_by_text(filterType, exact=True).nth(1).click()
    #  tupo click
    page.locator(".styles_title__nLZ-h").click()
    #  fill filter
    page.locator('[autocorrect=off]').nth(elementNumber).fill(filterName)
    page.wait_for_timeout(3000)
    #  choose filter
    page.get_by_text(filterName, exact=True).nth(0).click()


def add_notification(notificationType, page="page: Page"):
    #  add new
    page.locator(BLOCK_ADD_NEW_RULE).get_by_role("button").click()
    page.wait_for_selector(INPUT_NOTIFICATION_NAME)
    #  click to list
    page.locator('[class="css-8mmkcg"]').first.click()
    page.wait_for_timeout(300)
    #  choose type
    page.locator('[class=" css-164zrm5-menu"]').get_by_text(notificationType, exact=True).click()


def fill_attr_for_email(letterTheme, email, page="page: Page"):
    page.wait_for_selector(INPUT_LETTER_THEME)
    page.locator(INPUT_LETTER_THEME).fill(letterTheme)
    page.locator(INPUT_EMAIL).fill(email)


def fill_message(text, page="page: Page"):
    page.locator(INPUT_COMMENT).fill(text)
    page.locator('[aria-label="ID звонка. Пример: 123456789012345678901234"]').click()


def set_url_and_headers(url, headers, page="page: Page"):
    page.locator(INPUT_URL).fill(url)
    page.locator(INPUT_HEADERS).fill(headers)


def save_rule(page="page: Page"):
    page.get_by_role("button", name="Сохранить правило").click()
    page.wait_for_timeout(400)


def delete_rule(page="page: Page"):
    page.wait_for_selector(BUTTON_KORZINA)
    page.locator('[class*="sidebar"]').locator('[type="checkbox"]').first.click()
    page.locator(BUTTON_KORZINA).first.click()
    page.wait_for_timeout(500)
    #  confirm deleting
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(800)


def choose_block(blockNumber, page="page: Page"):
    page.locator(BUTTON_OPOVESHENIA).click()
    page.locator(".styles_root__qwOsd").locator(".styles_root__cx1Gi").nth(blockNumber).click()
    page.wait_for_selector(INPUT_NOTIFICATION_NAME)


def go_back_in_rule_after_save(notificationName, page="page: Page"):
    page.wait_for_selector('[class*=notifyList]')
    page.get_by_text(notificationName).click()
    page.wait_for_selector('[name="notifyTitle"]')


def change_api_method(originalMethod, newMethod, page="page: Page"):
    page.locator(BlOCK_API).get_by_text(originalMethod).click()
    page.get_by_text(newMethod, exact=True).click()


def go_to_user(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')