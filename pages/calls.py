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
INPUT_PO_TEGAM = "#react-select-12-input"
INPUT_PO_TEGAM_NEW = '//html/body/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/input'
INPUT_VREMYA_ZVONKA = "#react-select-10-input"
INPUT_DLITELNOST_ZVONKA = "#react-select-9-input"
INPUT_NOMER_CLIENTA = "#react-select-5-input"
INPUT_NOMER_SOTRUDNIKA = "#react-select-7-input"
INPUT_SLOVAR_ILI_TEXT_CLIENT = "#react-select-6-input"
INPUT_SLOVAR_ILI_TEXT_SOTRUDNIK = "#react-select-8-input"
INPUT_ID = "#react-select-11-input"
# buttons
BUTTON_ZVONKI = "button[value='calls']"
BUTTON_DOBAVIT_USLOVIE = "//button[contains(text(),'Добавить условие')]"
# other
NAYDENO_ZVONKOV = '//*[@id="root"]/div/div[2]/div/div[3]/div[1]/div/p'
POISK_PO_FRAGMENTAM = "//h6[contains(text(),'Поиск по фрагментам')]"
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


def find_calls(page="page: Page"):
    page.get_by_role("button", name="Найти коммуникации").click()
    page.wait_for_selector(NAYDENO_ZVONKOV, timeout=wait_until_visible)



def choose_period_button(period, page="page: Page"):
    page.wait_for_selector(period, timeout=wait_until_visible)
    page.locator(period).click()

def choose_preiod_date(firstDate, lastDate, page="page: Page"):
    page.locator(FIRST_DATE).click()
    page.locator(FIRST_DATE).fill(firstDate)
    page.wait_for_timeout(300)
    page.locator(LAST_DATE).click()
    page.locator(LAST_DATE).fill(lastDate)
    page.wait_for_timeout(300)
    page.keyboard.press("Enter")


def remove_filter_value(filterValue, page="page: Page"):
    page.locator(f'[aria-label="Remove {filterValue}"]').click()
    page.locator(POISK_PO_FRAGMENTAM).click()

def fill_search_length(value, page="page: Page"):
    page.locator(INPUT_DLITELNOST_ZVONKA).clear()
    page.locator(INPUT_DLITELNOST_ZVONKA).fill(value)

def change_sort(sortType, page="page: Page"):
    page.locator(CHANGE_SORT).click()
    page.get_by_text(sortType).click()
    page.wait_for_selector(FIRST_PAGE_PAGINATION, timeout=wait_until_visible)

