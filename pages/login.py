BUTTON_VOITI = "[type='submit']"

def quit_from_profile(page="page: Page"):
    page.locator('[aria-label="Профиль"]').get_by_role("button").click()
    page.get_by_text("Выйти", exact=True).click()