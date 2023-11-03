BUTTON_OPOVESHENIA = '[href*="/notifications"]'


BUTTON_KORZINA = '[aria-label="Удалить"]'

INPUT_NOTIFICATION_NAME = '[placeholder="Например: Жалоба на сотрудника"]'

INPUT_LETTER_THEME = '[placeholder="Укажите тему письма"]'
INPUT_EMAIL = '[placeholder="example@mail.com"]'
INPUT_HEADERS = '[placeholder="Можно проставить авторизацию и content-type"]'
INPUT_URL = '[placeholder="шаблон URL"]'

def set_notification_name(notificationName, page="page: Page"):
    page.locator(INPUT_NOTIFICATION_NAME).fill(notificationName)

def add_filter(filterType, filterName, page="page: Page"):
    #  dobavit filtr
    page.locator('[style="color: rgb(146, 84, 222);"]').click()
    #  choose po tegam
    page.locator(".css-woue3h-menu").get_by_text(filterType, exact=True).nth(1).click()
    #  tupo click
    page.locator(".styles_title__nLZ-h").click()
    #  fill filter
    page.locator('[autocorrect=off]').nth(0).fill(filterName)
    page.wait_for_timeout(3000)
    #  choose filter
    page.get_by_text(filterName, exact=True).nth(0).click()

def add_notification(notificationType, page="page: Page"):
    page.locator(BUTTON_OPOVESHENIA).click()
    #  add new
    page.locator(".styles_addNewRule__zhZVC").get_by_role("button").click()
    #  click to list
    page.locator('[class="css-8mmkcg"]').first.click()
    #  choose email
    page.locator('[class=" css-164zrm5-menu"]').get_by_text(notificationType, exact=True).click()

def fill_attr_for_email(letterTheme, email, page="page: Page"):
    page.locator(INPUT_LETTER_THEME).fill(letterTheme)
    page.locator(INPUT_EMAIL).fill(email)

def fill_message(text, page="page: Page"):
    page.locator('[class="styles_textarea__+sldQ"]').fill(text)
    page.locator('[aria-label="ID звонка. Пример: 123456789012345678901234"]').click()

def set_url_and_headers(url, headers, page="page: Page"):
    page.locator(INPUT_URL).fill(url)
    page.locator(INPUT_HEADERS).fill(headers)