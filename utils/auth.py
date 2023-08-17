def auth(login, password, page="page: Page"):
    page.locator("[id='mui-1']").fill(login)
    page.locator("[id='mui-2']").fill(password)
    page.locator("[id='mui-3']").click()
