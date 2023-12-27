def auth(login, password, page="page: Page"):
    page.wait_for_selector("[id='username']")
    page.locator("[id='username']").fill(login)
    page.wait_for_selector("[id='password']")
    page.locator("[id='password']").fill(password)
    page.wait_for_selector("[type='submit']")
    page.locator("[type='submit']").click()
