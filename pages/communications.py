from utils.variables import wait_until_visible


# time period
YESTERDAY = '[value="yesterday"]'
WEEK = '[value="this_week"]'
MONTH = '[value="this_month"]'
YEAR = '[value="this_year"]'
ALL_TIME = '[value="all_time"]'
FIRST_DATE = '[placeholder="Начальная дата"]'
LAST_DATE = '[placeholder="Конечная дата"]'

# inputs
INPUT_PO_TEGAM = '[data-testid="filters_search_by_tags"]'
INPUT_PO_TEGAM_NEW = '//html/body/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/input'
INPUT_VREMYA_ZVONKA = '[data-testid="filters_call_time_interval"]'
INPUT_DLITELNOST_ZVONKA = '[data-testid="filters_call_duration"]'
INPUT_NOMER_CLIENTA = '[data-testid="filters_client_phone"]'
INPUT_NOMER_SOTRUDNIKA = '[data-testid="filters_operator_phone"]'
INPUT_SLOVAR_ILI_TEXT_CLIENT = '[data-testid="filters_client_phrases"]'
INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK = '[data-testid="filters_operator_phrases"]'
INPUT_ID = '[data-testid="filters_any_id"]'
# buttons
BUTTON_ZVONKI = "button[value='calls']"
BUTTON_DOBAVIT_USLOVIE = "//button[contains(text(),'Добавить условие')]"
BUTTON_EXPAND_CALL = '[data-testid="call_expand"]'
# other
AUDIO_PLAYER = '[class*="react-audio-player"]'
NAYDENO_ZVONKOV = '//*[@id="root"]/div/div[2]/div/div[3]/div[1]/div/p'
POISK_PO_FRAGMENTAM = "//h6[contains(text(),'Поиск по коммуникациям')]"
CHANGE_LOGIC_OPERATOR = '//*[@id="root"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div[2]/div'
CALL_DATE_AND_TIME = '//html/body/div/div/div[2]/div/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[2]/div/p'

CHANGE_SORT = '//*[@id="root"]/div/div[2]/div/div[3]/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div'

FIRST_PAGE_PAGINATION = '[aria-label="page 1"]'


def change_filter(filterType, elementNumber, page="page: Page"):
    # button click
    page.locator(".css-b62m3t-container").get_by_text("Изменить фильтры").click()  # button click
    # choose filter with element number. first - 0, second - 1, etc
    page.locator(".css-woue3h-menu").get_by_text(filterType, exact=True).nth(elementNumber).click()


def choose_filter_value(filterValue, page="page: Page"):
    # input click
    page.locator("(//div[contains(@class,'css-12ol9ef')])[8]").first.click()
    # choose filter value
    page.locator(".css-1lq1yle-menu").get_by_text(filterValue).click()
    # tupo click
    page.locator(POISK_PO_FRAGMENTAM).click()


def press_find_communications(page="page: Page"):
    page.wait_for_timeout(200)
    page.locator('[data-testid="calls_btns_find"]').click()
    page.wait_for_timeout(300)
    page.wait_for_selector(NAYDENO_ZVONKOV, timeout=wait_until_visible)


def choose_period_button(period, page="page: Page"):
    page.wait_for_selector(period, timeout=wait_until_visible)
    page.locator(period).click()


def choose_preiod_date(firstDate, lastDate, page="page: Page"):
    page.wait_for_selector(INPUT_PO_TEGAM, timeout=wait_until_visible)
    page.locator(FIRST_DATE).click()
    page.wait_for_timeout(100)
    page.locator(FIRST_DATE).fill(firstDate)
    page.wait_for_timeout(300)
    page.locator(LAST_DATE).click()
    page.wait_for_timeout(100)
    page.locator(LAST_DATE).fill(lastDate)
    page.wait_for_timeout(300)
    page.keyboard.press("Enter")
    page.wait_for_timeout(300)

def remove_filter_value(filterValue, page="page: Page"):
    page.locator(f'[aria-label="Remove {filterValue}"]').click()
    page.locator(POISK_PO_FRAGMENTAM).click()


def fill_search_length(value, page="page: Page"):
    page.wait_for_timeout(200)
    page.locator(INPUT_DLITELNOST_ZVONKA).locator('[type="text"]').clear()
    page.wait_for_timeout(200)
    page.locator(INPUT_DLITELNOST_ZVONKA).locator('[type="text"]').fill(value)
    page.wait_for_timeout(200)


def change_sort(sortType, page="page: Page"):
    page.locator(CHANGE_SORT).click()
    page.get_by_text(sortType).click()
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

