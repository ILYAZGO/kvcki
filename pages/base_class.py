from playwright.sync_api import Page, expect


class BaseClass:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 50000
        self.users_list = page.locator("#react-select-2-input")
        self.login = page.locator('[id="username"]')
        self.password = page.locator('[id="password"]')
        self.button_enter = page.locator('[type="submit"]')

    def navigate(self, url):
        """Opens main page"""
        self.page.goto(url, timeout=self.timeout)

    def auth(self, login, password):
        """Auth"""
        self.page.wait_for_selector("[id='username']")
        self.login.type(login, delay=20)
        self.page.wait_for_selector("[id='password']")
        self.password.type(password, delay=20)
        self.page.wait_for_selector("[type='submit']")
        self.button_enter.click()
        self.page.wait_for_timeout(1000)

    def go_to_user(self, name):
        """Change user"""
        self.users_list.type(name, delay=30)
        self.page.get_by_text(name, exact=True).click()
        self.page.wait_for_selector('[class*="CallsHeader"]')


