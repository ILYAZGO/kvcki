BUTTON_RAZMETKA = '[value="tags"]'
USERS_LIST = "#react-select-2-input"

'''locators for rules'''
'''---------------------------------------'''
# inputs
INPUT_POISK = '[name="searchString"]'
INPUT_NEW_GROUP_NAME = '[name="groupName"]'
INPUT_EDIT_GROUP_NAME = "//input[@value='12345']"
INPUT_NAZVANIE_TEGA = '[data-testid="markup_newRuleInput"]'
INPUT_CHOOSE_USER_FOR_IMPORT = '[data-testid="markup_importUserSelect"]'

# buttons

BUTTON_DOBAVIT_GRUPPU = '[data-testid="markup_addGroup"]'
BUTTON_DOBAVIT_TEG = '[data-testid="markup_addTag"]'
BUTTON_OTMENA = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]"
BUTTON_KRESTIK = '[data-testid="CloseIcon"]'
BUTTON_LUPA = "//button[@type='submit']//*[name()='svg']"
BUTTON_OTPRAVIT = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[1]"
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"
BUTTON_KORZINA = '[aria-label="Удалить"]'

BUTTON_IMPORTIROVAT_PRAVILA = '[data-testid="markup_importTagRules"]'
# other
CLICK_NEW_GROUP = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div'
NI4EGO_NE_NAYDENO = ".styles_noFound__0AI5V"
NAZVANIE_PRAVILA_TEGIROVANIYA = NAZVANIE_SLOVARYA = '[name="title"]'

'''locators for dictionaries'''
'''---------------------------------------------'''
# inputs
INPUT_NAZVANIE_SLOVAR = '[name="dictName"]'
INPUT_SPISOK_SLOV = '[name="phrases"]'
# buttons
BUTTON_SLOVARI = '[data-testid="markup_nav_dicts"]'
BUTTON_DOBAVIT_SLOVAR = '[data-testid="markup_addDict"]'
BUTTON_IMPORTIROVAT_SLOVARI = '[data-testid="markup_importDicts"]'
# other
CLICK_ON_GROUP = "//p[normalize-space()='12345']"



'''locators for check-lists'''
# inputs
INPUT_CHECK_LIST_NAME = "[name='title']"
# buttons

BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_DOBAVIT_CHECK_LIST = '[data-testid="markup_addChecklists"]'


def create_group(groupName, page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_GRUPPU)
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill(groupName)
    page.locator(BUTTON_OTPRAVIT).click()
    page.wait_for_timeout(1500)

def go_to_markup(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()

def go_to_dicts(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_SLOVARI).click()
    page.wait_for_timeout(1000)

def delete_group_and_rule_or_dict(page="page: Page"):
    page.locator(".css-izdlur").click()
    page.get_by_text("Удалить", exact=True).click()
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(2000)
    page.locator(BUTTON_KORZINA).click()