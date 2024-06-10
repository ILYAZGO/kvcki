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
BUTTON_DOBAVIT_TEG = '[data-testid="markup_addTaggingRule"]'
BUTTON_OTMENA = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]"
BUTTON_KRESTIK = '[data-testid="CloseIcon"]'
BUTTON_LUPA = "//button[@type='submit']//*[name()='svg']"
BUTTON_OTPRAVIT = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[1]"
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"
BUTTON_KORZINA = '[aria-label="Удалить"]'
BUTTON_ADD_SEQUENCE = '[data-testid="addNewTagSequenceItemBtn"]'
BUTTON_DELETE_SEQUENCE = '[data-testid="TagSequenceDeleteItem"]'
LIST_PRESENCE_ONE_OF_TAGS = '[data-testid="presenceOfOneOfTags"]'
LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER = '[data-testid="presenceOfOneOfTagsInSpecifiedIntervalAfter"]'
INPUT_INTERVAL_BETWEEN_TAGS = '[data-testid="intervalBetweenTags"]'
CHECK_BOX_ABSENCE_OF_TAGS = '[data-testid="triggeredInAbsenceOfTags"]'
CHECK_BOX_REVERSE_LOGIC = '[data-testid="reverseLogic"]'

BUTTON_IMPORTIROVAT_PRAVILA = '[data-testid="markup_importTagRules"]'
# other
CLICK_NEW_GROUP = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div'
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'
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


def go_to_user(name:str, page="page: Page"):
    page.locator(USERS_LIST).fill(name)
    page.wait_for_timeout(500)
    page.get_by_text(name, exact=True).click()
    page.wait_for_selector('[class*="CallsHeader"]')


def create_group(groupName, page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_GRUPPU)
    page.locator(BUTTON_DOBAVIT_GRUPPU).click()
    page.locator(INPUT_NEW_GROUP_NAME).fill(groupName)
    page.locator(BUTTON_OTPRAVIT).click()
    page.wait_for_timeout(1400)


def create_rule(ruleName, page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type(ruleName)
    #page.get_by_role("button", name="Отправить").click()
    page.keyboard.press('Enter')  # kostil'
    page.wait_for_timeout(1300)
    #page.get_by_role("button", name="Сохранить").click()
    page.wait_for_selector('[data-testid="tagSequenceBlock"]')


def go_to_markup(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_selector(BUTTON_DOBAVIT_GRUPPU)


def go_to_dicts(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.wait_for_selector(BUTTON_SLOVARI)
    page.locator(BUTTON_SLOVARI).click()
    page.wait_for_selector(BUTTON_DOBAVIT_SLOVAR)
    #page.wait_for_timeout(1000)


def delete_group_and_rule_or_dict(page="page: Page"):
    #page.locator(".css-izdlur").click()
    #page.get_by_text("Удалить", exact=True).click()
    page.locator('[width="30"]').click()
    page.wait_for_timeout(500)
    page.get_by_role("button", name="Удалить").click()
    page.wait_for_timeout(1500)
    page.locator(BUTTON_KORZINA).click()


def create_dict(dictName, page="page: Page"):
    page.locator(BUTTON_DOBAVIT_SLOVAR).click()
    page.locator(INPUT_NAZVANIE_SLOVAR).fill(dictName)
    page.get_by_role('button', name="Отправить").click()
    page.wait_for_timeout(1000)
    page.locator(INPUT_SPISOK_SLOV).fill("random_text")
    page.get_by_role("button", name="Сохранить").click()


def fill_what_said(text, page="page: Page"):
    page.locator('[data-testid="fragmentRuleWhatSaid"]').locator('[autocorrect="off"]').fill(text)
    page.keyboard.press("Enter")


def add_additional_terms(list, page="page: Page"):
    page.locator('[data-testid="fragmentRuleAddButton"]').get_by_role("button").dblclick()
    page.wait_for_selector('[id*="listbox"]')
    for i in list:
        page.locator('[id*="listbox"]').get_by_text(i).click()
    page.locator('[data-testid="fromStart"]').click()
    page.locator('[data-testid="onlyFirstMatch"]').click()
    for l in range(10):
        page.locator('[placeholder=">X, <X или X-Y. Время в секундах"]').nth(l).fill(f"{l}")
    page.wait_for_timeout(500)


def change_dict_type(currentType, nextType, page="page: Page"):
    page.get_by_text(currentType, exact=True).click()
    page.locator('[class*="-menu"]').get_by_text(nextType, exact=True).click()