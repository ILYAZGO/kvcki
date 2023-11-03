def auth(login, password, page="page: Page"):
    page.wait_for_locator("[id='mui-1']")
    page.locator("[id='mui-1']").fill(login)
    page.wait_for_locator("[id='mui-2']")
    page.locator("[id='mui-2']").fill(password)
    page.wait_for_locator("[id='mui-3']")
    page.locator("[id='mui-3']").click()
