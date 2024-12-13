def auth(login, password, page="page: Page"):
    page.wait_for_selector("[id='username']")
    page.locator("[id='username']").type(login, delay=10)
    page.wait_for_selector("[id='password']")
    page.locator("[id='password']").type(password, delay=10)
    page.wait_for_selector("[type='submit']")
    page.locator("[type='submit']").click()
    page.wait_for_timeout(1000)
