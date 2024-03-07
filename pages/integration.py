USEDESK_TOKEN = "445ab1e8e6853d3bbedf686ab02f4cb746098a9a"

USERS_LIST = "#react-select-2-input"
INPUT_API_TOKEN = '[data-testid="api_token"]'
INPUT_CALLS_LIMIT = '[name="maxNewCalls"]'

BUTTON_INTEGRACII_IN_MENU = '[href*="settings/integrations"]'
BUTTON_PODKLU4IT = ".styles_goToIntegrationsList__KXaHU"
BUTTON_SAVE_TOKEN = '[data-testid="AccessKeysTab_submit"]'
BUTTON_INTEGRACII = ".styles_firstTitle__iaGwm"
BUTTON_PLAY = "//div[@class='styles_buttonsWrapper__5BGen']//div[1]//button[1]"
BUTTON_SOZDAT = '[data-testid="StartTaskModalContent_submit"]'
BUTTON_FIND_CALLS = "(//button[contains(text(),'Найти коммуникации')])[1]"
BUTTON_KORZINA = "div[class='styles_button__xgQ1q'] button[type='button']"
BUTTON_UDALIT_INTEGRACIYU = '[data-testid="SettingsCell_deleteBtn"]'


NA4ALNAYA_DATA = "//input[@placeholder='Начальная дата']"
BUTTON_OK_IN_DATE = "button[class='ant-btn ant-btn-primary ant-btn-sm']"
NAYDENO_ZVONKOV_INTEGRATION = '//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/p'
LOGIN_IN_LEFT_MENU = ".MuiTypography-root.MuiTypography-body1.styles_headerLogin__eWAxf.css-pd9d9b"


def go_to_user(name, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(300)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')


def input_save_api_token(page="page: Page"):
    page.wait_for_selector(INPUT_API_TOKEN)
    page.locator(INPUT_API_TOKEN).locator('[type="text"]').fill(USEDESK_TOKEN)
    page.locator(BUTTON_SAVE_TOKEN).click()


def set_date(firstDate, page="page: Page"):
    page.locator(NA4ALNAYA_DATA).click()
    page.locator(NA4ALNAYA_DATA).fill(firstDate)
    page.wait_for_timeout(1300)
    page.locator(BUTTON_OK_IN_DATE).click()  #click ok
    page.wait_for_timeout(2500)
    page.locator(BUTTON_OK_IN_DATE).click()
    page.wait_for_timeout(1300)


def set_calls_limit(callsLimit, page="page: Page"):
    page.locator(INPUT_CALLS_LIMIT).fill(callsLimit)


def delete_integration(page="page: Page"):
    page.locator(BUTTON_KORZINA).click()
    page.wait_for_timeout(1000)
    page.locator(BUTTON_UDALIT_INTEGRACIYU).click()
    page.wait_for_timeout(1000)

