from playwright.sync_api import Page, expect

#from pages.reports import FIRST_DATE


class BaseClass:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 70000
        self.users_list = page.locator("#react-select-2-input")
        self.login = page.locator('[id="username"]')
        self.password = page.locator('[id="password"]')
        self.button_enter = page.locator('[type="submit"]')
        self.menu = page.locator('[class*="-menu"]')
        self.snackbar = page.locator('[class*="SnackbarItem"]')
        '''Dates and calendar'''
        self.yesterday = page.locator('[value="yesterday"]')
        self.week = page.locator('[value="this_week"]')
        self.month = page.locator('[value="this_month"]')
        self.year = page.locator('[value="this_year"]')
        self.all_time = page.locator('[value="all_time"]')
        self.first_date = page.locator('[placeholder="Начальная дата"]')
        self.last_date = page.locator('[placeholder="Конечная дата"]')

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
        self.page.wait_for_timeout(2000)

    def go_to_user(self, name: str):
        """Change user"""
        self.users_list.type(name, delay=30)
        self.page.get_by_text(name, exact=True).click()
        self.page.wait_for_selector('[class*="CallsHeader"]')

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
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press(key)
        self.page.wait_for_timeout(1000)

    def check_alert(self, message: str):
        self.snackbar.wait_for(state="visible", timeout=self.timeout)
        expect(self.snackbar).to_contain_text(message)
        self.snackbar.wait_for(state="hidden", timeout=self.timeout)


