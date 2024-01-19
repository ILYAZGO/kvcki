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
BUTTON_ADD_DISABLED = '[style="cursor: not-allowed;"]'

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

def create_rule(ruleName, page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type(ruleName)
    page.keyboard.press('Enter')  # kostil'
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


def create_dict(dictName, page="page: Page"):
    page.locator(BUTTON_DOBAVIT_SLOVAR).click()
    page.locator(INPUT_NAZVANIE_SLOVAR).fill(dictName)
    page.get_by_role('button', name="Отправить").click()
    page.wait_for_timeout(1000)
    page.locator(INPUT_SPISOK_SLOV).fill("random_text")




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
INPUT_LEFT_CHECK_LIST_NAME = "//input[@value='12345']"
# buttons

BUTTON_CHECK_LIST = '[data-testid="markup_nav_checklists"]'
BUTTON_DOBAVIT_CHECK_LIST = '[data-testid="markup_addChecklists"]'
BUTTON_SAVE = ".MuiButton-contained"
#BUTTON_ADD_ANSWER = ".styles_addBtn__LzsSV"
#BUTTON_ADD_QUESTION = ".styles_addBtn__rsxfc"
#BUTTON_DELETE_QUESTION = ".styles_deleteBtn__8Tkl6"


#  creates first question with 2 answers and points and second question with answer and points then delete second question
def create_check_list_with_questions_and_answers(checkListName, firstQustionTitle, secondQuestionTitle, page="page: Page"):
    # create check-list
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_CHECK_LIST).click()
    page.wait_for_selector(BUTTON_DOBAVIT_CHECK_LIST)
    page.locator(BUTTON_DOBAVIT_CHECK_LIST).click()
    page.wait_for_selector(INPUT_CHECK_LIST_NAME)
    page.locator(INPUT_CHECK_LIST_NAME).fill(checkListName)
    # add questions
    page.locator('[class="styles_content__4ydtX"]').nth(1).get_by_role("button").click()

    page.locator(INPUT_FIRST_QUESTION).fill(firstQustionTitle)
    page.locator(INPUT_FIRST_ANSWER).fill("Answer1")
    page.locator(INPUT_FIRST_POINTS).fill("1")
    #page.locator(BUTTON_ADD_ANSWER).click()
    page.get_by_role("button", name="Добавить ответ").click()
    page.locator(INPUT_SECOND_ANSWER).fill("Answer2")
    page.locator(INPUT_SECOND_POINTS).fill("2")
    #page.locator(BUTTON_ADD_QUESTION).click()
    page.get_by_role("button", name="Добавить вопрос").click()
    page.locator(INPUT_SECOND_QUESTION).fill(secondQuestionTitle)
    page.locator(INPUT_THIRD_ANSWER).fill("Answer3")
    page.locator(INPUT_THIRD_POINTS).fill("3")
    #page.locator(BUTTON_DELETE_QUESTION).nth(1).click()
    page.get_by_role("button", name="Удалить вопрос").nth(1).click()

    # save
    page.locator(BUTTON_SAVE).click()

def create_delete_appriser(title, page="page: Page"):

    page.locator('[class*="CheckListAppraisers_addBtn"]').click()
    page.locator('[name="appraisers.0.title"]').fill(title)
    page.locator('[name="appraisers.0.points"]').fill("5")
    page.locator('[class*="CheckListAppraisers_deleteBtn"]')

def delete_check_list(page="page: Page"):
    page.locator(BUTTON_KORZINA).click()
    page.get_by_role("button", name="Удалить").click()


#  all for gpt


BUTTON_GPT = '[data-testid="markup_nav_gpt"]'
BUTTON_GPT_CREATE_RULE = '[data-testid="markup_addGroup"]'
BUTTON_GPT_SAVE = '[data-testid="acceptButton"]'

INPUT_GPT_RULE_NAME = '[placeholder="Название правила"]'
INPUT_GPT_TEG_NAME = '[placeholder="Название тега"]'
INPUT_GPT_QUESTION = '[placeholder="Сформулируйте свой вопрос..."]'

def go_to_gpt(page="page: Page"):
    page.wait_for_selector(BUTTON_RAZMETKA)
    page.locator(BUTTON_RAZMETKA).click()
    page.locator(BUTTON_GPT).click()
    page.wait_for_timeout(1000)

def create_gpt_rule_with_one(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)

    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")

    page.locator(BUTTON_GPT_SAVE).click()
    page.wait_for_timeout(1000)


# create group with 2 tags with 2 questions inside
def create_gpt_rule_with_two(GptRuleName, page="page: Page"):
    page.locator(BUTTON_GPT_CREATE_RULE).click()
    page.wait_for_selector(INPUT_GPT_RULE_NAME)
    page.locator(INPUT_GPT_RULE_NAME).fill(GptRuleName)
    page.wait_for_timeout(700)
    page.locator(INPUT_GPT_TEG_NAME).fill("GPTteg1")
    page.locator(INPUT_GPT_QUESTION).fill("GPTquestion1")
    page.get_by_role("button", name="Добавить вопрос").click()
    page.locator(INPUT_GPT_TEG_NAME).nth(1).fill("GPTteg2")
    page.locator(INPUT_GPT_QUESTION).nth(1).fill("GPTquestion2")
    page.keyboard.press("PageDown")
    page.locator(BUTTON_GPT_SAVE).click(force=True)
    page.wait_for_timeout(1000)

def turn_on_rule(page="page: Page"):
    page.locator('[aria-label="Вкл/Выкл"]').locator('[type="checkbox"]').click()
    page.wait_for_timeout(1500)