#from utils.variables import wait_until_visible

from pages.base_class import *
from playwright.sync_api import Page, expect

BUTTON_MARKUP = '[value="tags"]'
BUTTON_DICTS = '[data-testid="markup_nav_dicts"]'
BUTTON_ADD_GROUP = '[data-testid="markup_addGroup"]'
INPUT_NEW_GROUP_NAME = '[name="groupName"]'
BUTTON_ADD_DICT = '[data-testid="markup_addDict"]'
INPUT_DICT_NAME = '[name="dictName"]'
INPUT_WORDS_LIST = '[name="phrases"]'

class Dicts(BaseClass):
    def __init__(self, page: Page):
        BaseClass.__init__(self, page)
        self.button_markup = page.locator(BUTTON_MARKUP)
        self.button_dicts = page.locator(BUTTON_DICTS)
        self.button_add_group = page.locator(BUTTON_ADD_GROUP)
        self.input_new_group_name = page.locator(INPUT_NEW_GROUP_NAME)
        self.input_dict_name = page.locator(INPUT_DICT_NAME)
        self.input_words_list = page.locator(INPUT_WORDS_LIST)
        self.button_add_dict = page.locator(BUTTON_ADD_DICT)


    def go_to_dicts(self):
        self.page.wait_for_selector(BUTTON_MARKUP)
        self.button_markup.click()
        self.page.wait_for_selector(BUTTON_DICTS)
        self.button_dicts.click()
        self.page.wait_for_selector(BUTTON_ADD_DICT)
        self.page.wait_for_load_state(state="load", timeout=self.timeout)

    def create_group(self, group_name: str):
        self.page.wait_for_selector(BUTTON_ADD_GROUP)
        self.button_add_group.click()
        self.page.wait_for_selector(INPUT_NEW_GROUP_NAME)
        self.input_new_group_name.type(group_name, delay=30)
        self.modal_window.locator(BUTTON_SUBMIT).click()
        self.page.wait_for_timeout(500)

    def create_dict(self, dict_name: str, text: str):
        self.button_add_dict.click()
        self.page.wait_for_selector(INPUT_DICT_NAME)
        self.input_dict_name.type(dict_name, delay=30)
        self.modal_window.locator(BUTTON_SUBMIT).click()
        self.page.wait_for_selector(INPUT_WORDS_LIST)
        self.input_words_list.type(text, delay=30)

'''------locators for rules---------'''
# inputs

INPUT_EDIT_GROUP_NAME = "//input[@value='12345']"
INPUT_NAZVANIE_TEGA = '[data-testid="markup_newRuleInput"]'
INPUT_CHOOSE_USER_FOR_IMPORT = '[data-testid="markup_importUserSelect"]'

# buttons
BUTTON_DOBAVIT_TEG = '[data-testid="markup_addTaggingRule"]'
BUTTON_OTMENA = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]"
BUTTON_LUPA = "//button[@type='submit']//*[name()='svg']"
BUTTON_PENCIL = '[aria-label="Изменить название"]'
BUTTON_SAVE_EDITED_NAME = ".styles_root__4Hw2A"
BUTTON_KORZINA = '[aria-label="Удалить"]'
# other
GROUP_LIST = '[class*="styles_dpBothBox_"]'
ACTIVE_GROUP = '[class*="styles_isActive_"]'
CLICK_NEW_GROUP = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div'
NI4EGO_NE_NAYDENO = '[class*="styles_noFound"]'
NAZVANIE_SLOVARYA = '[name="title"]'

TOOLTIP_BUTTON_DOBAVIT_SLOVAR = '[aria-label="Чтобы добвить словарь, выберите или добавьте группу."]'
BUTTON_IMPORTIROVAT_SLOVARI = '[data-testid="markup_importDicts"]'
# other
CLICK_ON_GROUP = "//p[normalize-space()='12345']"

def delete_rule_or_dict(page="page: Page"):
    #page.locator(".css-izdlur").click()
    #page.get_by_text("Удалить", exact=True).click()
    page.locator('[width="30"]').click()
    page.wait_for_selector(MODAL_WINDOW)
    page.locator(MODAL_WINDOW).get_by_role("button", name="Удалить").click()
    page.wait_for_selector(MODAL_WINDOW, state="hidden")

def delete_group(page="page: Page"):
    page.locator(ACTIVE_GROUP).locator(BUTTON_KORZINA).click()

def change_dict_type(currentType, nextType, page="page: Page"):
    page.get_by_text(currentType, exact=True).click()
    page.wait_for_timeout(300)
    page.locator('[class*="-menu"]').get_by_text(nextType, exact=True).click()
    page.wait_for_timeout(300)

