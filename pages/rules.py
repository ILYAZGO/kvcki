from pages.base_class import *
from playwright.sync_api import Page, expect

BUTTON_ADD_GROUP = '[data-testid="markup_addGroup"]'
INPUT_NEW_GROUP_NAME = '[name="groupName"]'
ACTIVE_GROUP = '[class*="styles_isActive_"]'

class Rules(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_add_group = page.locator(BUTTON_ADD_GROUP)
        self.input_new_group_name = page.locator(INPUT_NEW_GROUP_NAME)

    def create_group(self, group_name: str):
        self.page.wait_for_selector(BUTTON_ADD_GROUP)
        self.button_add_group.click()
        self.page.wait_for_selector(INPUT_NEW_GROUP_NAME)
        self.input_new_group_name.type(group_name, delay=30)
        self.modal_window.locator(BUTTON_SUBMIT).click()
        self.page.wait_for_timeout(500)

    def delete_group(self):
        self.page.locator(ACTIVE_GROUP).locator(BUTTON_KORZINA).click()
        self.page.wait_for_timeout(500)

    def delete_rule_or_dict(self):
        self.page.locator('[width="30"]').click()
        self.page.wait_for_selector(MODAL_WINDOW)
        self.modal_window.get_by_role("button", name="Удалить").click()
        self.page.wait_for_selector(MODAL_WINDOW, state="hidden")

# inputs
INPUT_EDIT_GROUP_NAME = "//input[@value='12345']"
INPUT_NAZVANIE_TEGA = '[data-testid="markup_newRuleInput"]'
INPUT_CHOOSE_USER_FOR_IMPORT = '[data-testid="markup_importUserSelect"]'

# buttons
BUTTON_DOBAVIT_TEG = '[data-testid="markup_addTaggingRule"]'
BUTTON_OTMENA = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]"
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"
BUTTON_ADD_SEQUENCE = '[data-testid="addNewTagSequenceItemBtn"]'
BUTTON_DELETE_SEQUENCE = '[data-testid="TagSequenceDeleteItem"]'
LIST_PRESENCE_ONE_OF_TAGS = '[data-testid="presenceOfOneOfTags"]'
LIST_PRESENCE_ONE_OF_TAGS_IN_INTERVAL_AFTER = '[data-testid="presenceOfOneOfTagsInSpecifiedIntervalAfter"]'
INPUT_INTERVAL_BETWEEN_TAGS = '[data-testid="intervalBetweenTags"]'
CHECK_BOX_ABSENCE_OF_TAGS = '[data-testid="triggeredInAbsenceOfTags"]'
CHECK_BOX_REVERSE_LOGIC = '[data-testid="reverseLogic"]'
BUTTON_IMPORTIROVAT_PRAVILA = '[data-testid="markup_importTagRules"]'
GROUP_LIST = '[class*="styles_dpBothBox_"]'

CLICK_NEW_GROUP = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div'
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'
NAZVANIE_PRAVILA_TEGIROVANIYA = NAZVANIE_SLOVARYA = '[name="title"]'

def create_rule(ruleName, page="page: Page"):
    page.wait_for_selector(BUTTON_DOBAVIT_TEG)
    page.locator(BUTTON_DOBAVIT_TEG).click()
    page.wait_for_selector(INPUT_NAZVANIE_TEGA)
    page.locator(INPUT_NAZVANIE_TEGA).type(ruleName, delay=40)
    #page.get_by_role("button", name="Отправить").click()
    page.keyboard.press('Enter')  # kostil'
    page.wait_for_timeout(1300)
    #page.get_by_role("button", name="Сохранить").click()
    #page.wait_for_selector('[data-testid="tagSequenceBlock"]')

def fill_what_said(text, page="page: Page"):
    page.locator('[data-testid="fragmentRuleWhatSaid"]').locator('[autocorrect="off"]').type(text, delay=30)
    page.keyboard.press("Enter", delay=30)
    page.wait_for_timeout(500)

def add_additional_terms(list, page="page: Page"):
    page.locator('[data-testid="fragmentRuleAddButton"]').get_by_role("button").dblclick()
    page.wait_for_selector('[class*="-menu"]')
    for i in list:
        page.locator('[class*="-menu"]').get_by_text(i).click()
    page.locator('[data-testid="fromStart"]').click()
    page.locator('[data-testid="onlyFirstMatch"]').click()
    for l in range(10):
        page.locator('[placeholder=">X, <X или X-Y. Время в секундах"]').nth(l).fill(f"{l}")
    page.wait_for_timeout(500)


