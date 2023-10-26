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



#  all for check-lists

'''locators for check-lists'''
# inputs
INPUT_CHECK_LIST_NAME = "[name='title']"
INPUT_FIRST_QUESTION = "[name='questions.0.title']"
INPUT_SECOND_QUESTION = "[name='questions.1.title']"
INPUT_FIRST_ANSWER = '[name="questions.0.answers.0.answer"]'
INPUT_SECOND_ANSWER = '[name="questions.0.answers.1.answer"]'
INPUT_THIRD_ANSWER = '[name="questions.1.answers.0.answer"]'
INPUT_FIRST_POINTS = '[name="questions.0.answers.0.point"]'
INPUT_SECOND_POINTS = '[name="questions.0.answers.1.point"]'
INPUT_THIRD_POINTS = '[name="questions.1.answers.0.point"]'
# buttons

BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_DOBAVIT_CHECK_LIST = '[data-testid="markup_addChecklists"]'
BUTTON_SAVE = ".MuiButton-contained"
BUTTON_ADD_ANSWER = ".styles_addBtn__fYwu9"
BUTTON_ADD_QUESTION = ".styles_addBtn__jkLM3"


def create_questions_and_answers(firstQustionTitle, secondQuestionTitle, page="page: Page"):
    #  creates first question with 2 answers and points and second question with answer and points then delete second question
    page.locator('[class="styles_content__4ydtX"]').nth(1).get_by_role("button").click()  # add questions

    page.locator(INPUT_FIRST_QUESTION).fill(firstQustionTitle)
    page.locator(INPUT_FIRST_ANSWER).fill("Answer1")
    page.locator(INPUT_FIRST_POINTS).fill("1")
    page.locator(BUTTON_ADD_ANSWER).click()
    page.locator(INPUT_SECOND_ANSWER).fill("Answer2")
    page.locator(INPUT_SECOND_POINTS).fill("2")
    page.locator(BUTTON_ADD_QUESTION).click()
    page.locator(INPUT_SECOND_QUESTION).fill(secondQuestionTitle)
    page.locator(INPUT_THIRD_ANSWER).fill("Answer3")
    page.locator(INPUT_THIRD_POINTS).fill("3")
    page.locator(".styles_deleteBtn__bPjk5").nth(1).click()

def create_delete_appriser(title, page="page: Page"):

    page.locator('[class*="CheckListAppraisers_addBtn"]').click()
    page.locator('[name="appraisers.0.title"]').fill(title)
    page.locator('[name="appraisers.0.points"]').fill("5")
    page.locator('[class*="CheckListAppraisers_deleteBtn"]')

def delete_check_list(page="page: Page"):
    page.locator(BUTTON_KORZINA).click()
    page.get_by_role("button", name="Удалить").click()
