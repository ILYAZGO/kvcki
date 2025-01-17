from playwright.sync_api import Page, expect

BUTTON_COMMUNICATIONS = '[value="calls"]'
BUTTON_REPORTS = '[value="reports"]'
BUTTON_MARKUP = '[value="tags"]'
BUTTON_NOTIFICATIONS = '[value="notifications"]'
BUTTON_SETTINGS = '[value="settings"]'
BUTTON_FIND_COMMUNICATIONS = '[data-testid="calls_btns_find"]'
BUTTON_EMPLOYEES = '[href*="settings/employees"]'
BUTTON_SUBMIT = '[type="submit"]'
MENU = '[class*="-menu"]'
MODAL_WINDOW = '[role="dialog"]'
BUTTON_CROSS = '[data-testid="CloseIcon"]'
INPUT_SEARCH = '[name="searchString"]'
BUTTON_KORZINA = '[aria-label="Удалить"]'

SELECT_LANGUAGE = '[data-testid="stt_language"]'
SELECT_ENGINE = '[data-testid="stt_engine"]'
SELECT_MODEL = '[data-testid="stt_model"]'

INPUT_NAME = '[name="name"]'
INPUT_LOGIN = '[name="login"]'
INPUT_PASSWORD = '[name="password"]'
INPUT_EMAIL = '[name="email"]'
INPUT_PHONE = '[name="phoneNumber"]'
INPUT_COMMENT = '[name="comment"]'
SELECT_ROLE = '[data-testid="selectRole"]'

class BaseClass:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 40000
        self.users_list = page.locator("#react-select-2-input")
        self.login = page.locator('[id="username"]')
        self.password = page.locator('[id="password"]')
        self.button_enter = page.locator(BUTTON_SUBMIT)
        self.menu = page.locator(MENU)
        self.modal_window = page.locator(MODAL_WINDOW)
        self.snackbar = page.locator('[class*="SnackbarItem-wrappedRoot"]')
        '''Dates and calendar'''
        self.yesterday = page.locator('[value="yesterday"]')
        self.week = page.locator('[value="this_week"]')
        self.month = page.locator('[value="this_month"]')
        self.year = page.locator('[value="this_year"]')
        self.all_time = page.locator('[value="all_time"]')
        self.first_date = page.locator('[placeholder="Начальная дата"]')
        self.last_date = page.locator('[placeholder="Конечная дата"]')
        '''Word processing'''
        self.select_language = page.locator(SELECT_LANGUAGE).locator('[type="text"]')
        self.select_engine = page.locator(SELECT_ENGINE).locator('[type="text"]')
        self.select_model = page.locator(SELECT_MODEL).locator('[type="text"]')
        '''User info'''
        self.input_login = page.locator(INPUT_LOGIN)
        self.input_name = page.locator(INPUT_NAME)
        self.input_email = page.locator(INPUT_EMAIL)
        self.input_phone = page.locator(INPUT_PHONE)
        self.input_comment = page.locator(INPUT_COMMENT)
        self.input_password = page.locator(INPUT_PASSWORD)
        '''Other'''
        self.button_markup = page.locator(BUTTON_MARKUP)
        self.button_korzina = page.locator(BUTTON_KORZINA)
        self.button_employees = page.locator(BUTTON_EMPLOYEES)


    def navigate(self, url: str):
        """Opens main page"""
        #self.page.route('**/*.png', lambda route: route.abort())
        self.page.goto(url, timeout=self.timeout)

    def auth(self, login: str, password: str):
        """Auth"""
        self.page.wait_for_selector("[id='username']")
        self.login.type(login, delay=20)
        self.page.wait_for_selector("[id='password']")
        self.password.type(password, delay=20)
        self.page.wait_for_selector("[type='submit']")
        self.button_enter.click()
        self.page.wait_for_timeout(1000)
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(1000)

    def reload_page(self):
        """Reload page, wait for load and 1 second more"""
        self.page.reload()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(1500)

    def go_to_user(self, name: str):
        """Change user"""
        self.users_list.type(name, delay=30)
        self.page.get_by_text(name, exact=True).click()
        #self.page.wait_for_selector('[class*="CallsHeader"]')
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(2000)

    def choose_period_date(self, first_date: str, last_date: str):
        """Choose period"""
        self.page.wait_for_timeout(1500)
        self.page.wait_for_selector('[class="ant-space-item"]')
        self.page.wait_for_timeout(2000)
        self.first_date.click()
        self.page.wait_for_timeout(300)
        self.first_date.fill(first_date)
        self.page.wait_for_timeout(300)
        self.last_date.click()
        self.page.wait_for_timeout(300)
        self.last_date.fill(last_date)
        self.page.wait_for_timeout(300)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(300)

    def press_key(self, key: str):
        """Press key on keyboard"""
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press(key)
        self.page.wait_for_timeout(1000)

    def check_alert(self, message: str):
        """Wait snackbar, check text, wait for close"""
        self.snackbar.wait_for(state="visible", timeout=self.timeout)
        expect(self.snackbar).to_contain_text(message)
        self.snackbar.wait_for(state="hidden", timeout=self.timeout)

    def click_notifications(self):
        """Click Notifications"""
        self.page.wait_for_selector(BUTTON_NOTIFICATIONS, timeout=self.timeout)
        self.page.locator(BUTTON_NOTIFICATIONS).click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(500)

    def click_settings(self):
        """Click Settings"""
        self.page.wait_for_selector(BUTTON_SETTINGS, timeout=self.timeout)
        self.page.locator(BUTTON_SETTINGS).click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(INPUT_LOGIN, timeout=self.timeout)
        self.page.wait_for_timeout(500)

    def click_communications(self):
        """Click Communications"""
        self.page.wait_for_selector(BUTTON_COMMUNICATIONS, timeout=self.timeout)
        self.page.locator(BUTTON_COMMUNICATIONS).click()
        self.page.wait_for_timeout(500)
        self.page.wait_for_selector(BUTTON_FIND_COMMUNICATIONS)
        self.page.wait_for_timeout(500)

    def click_reports(self):
        """Click Reports"""
        self.page.wait_for_selector(BUTTON_REPORTS, timeout=self.timeout)
        self.page.wait_for_timeout(500)
        self.page.locator(BUTTON_REPORTS).click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(500)

    def click_markup(self):
        """Click Markup"""
        self.page.wait_for_selector(BUTTON_MARKUP)
        self.button_markup.click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_timeout(500)

    def click_employees(self):
        """Click employees in left menu"""
        self.button_employees.click()
        self.page.wait_for_load_state(state="load", timeout=self.timeout)
        self.page.wait_for_selector('[role="grid"]')

    def click_language_select(self):
        """Select language in word processing"""
        self.select_language.click()
        self.page.wait_for_selector(MENU)
        self.page.wait_for_timeout(300)

    def click_engine_select(self):
        """Select engine in word processing"""
        self.select_engine.click()
        self.page.wait_for_selector(MENU)
        self.page.wait_for_timeout(300)

    def click_model_select(self):
        """Select model in word processing"""
        self.select_model.click()
        self.page.wait_for_selector(MENU)
        self.page.wait_for_timeout(300)

    def choose_option(self, option_number: int):
        """Choose option from menu"""
        self.menu.locator(f'[id$="-option-{option_number}"]').click()

    def choose_user_import_from(self, username: str):
        self.page.locator('[class*="CustomSelect_simpleSelect"]').locator('[type="text"]').type(username, delay=20)
        self.menu.get_by_text(username, exact=True).click()
        self.page.wait_for_selector('[data-testid*="_importSearch}"]', timeout=self.timeout)

