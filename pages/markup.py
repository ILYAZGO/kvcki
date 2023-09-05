BUTTON_RAZMETKA = "//a[contains(text(),'Разметка')]"

'''locators for rules'''
'''---------------------------------------'''
# inputs
INPUT_POISK = '//html/body/div/div/div[2]/div/div/div[1]/div[2]/div[1]/form/div/div[1]/div[1]/div/input'
INPUT_NEW_GROUP_NAME = "//input[@name='groupName']"
INPUT_EDIT_GROUP_NAME = "//input[@value='12345']"
INPUT_NAZVANIE_TEGA = '[data-testid="markup_newRuleInput"]'

INPUT_CHOOSE_USER_FOR_IMPORT = "//html/body/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]/input"

# buttons

BUTTON_DOBAVIT_GRUPPU = '[data-testid="markup_addGroup"]'
BUTTON_DOBAVIT_TEG = '[data-testid="markup_addTag"]'
BUTTON_OTMENA = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[2]"
BUTTON_KRESTIK = "CloseIcon"
BUTTON_LUPA = "//button[@type='submit']//*[name()='svg']"
BUTTON_OTPRAVIT = "//html/body/div[2]/div[3]/div/div/div[2]/form/div[2]/button[1]"
BUTTON_PENCIL = "//div[@aria-label='Изменить название']//div//button[@type='button']//*[name()='svg']"
BUTTON_SAVE_EDITED_NAME = "(//button[@type='submit'])[1]"
BUTTON_KORZINA = "//div[@aria-label='Удалить']//div//button[@type='button']"

BUTTON_IMPORTIROVAT_PRAVILA = '[data-testid="markup_importTagRules"]'
# other
CLICK_NEW_GROUP = '//*[@id="root"]/div/div[2]/div/div/div[1]/div[1]/div[3]/div/div/div[2]/div'
NI4EGO_NE_NAYDENO =".styles_noFound__0AI5V"
NAZVANIE_PRAVILA_TEGIROVANIYA = "//input[@name='title']"

'''locators for dictionaries'''
'''---------------------------------------------'''
# inputs
INPUT_NAZVANIE_SLOVAR = "input[name='dictName']"
INPUT_SPISOK_SLOV = "textarea[name='phrases']"
# buttons
BUTTON_SLOVARI = '[data-testid="markup_nav_dicts"]'
BUTTON_DOBAVIT_SLOVAR = '[data-testid="markup_addDict"]'
BUTTON_IMPORTIROVAT_SLOVARI = '[data-testid="markup_importDicts"]'
# other
CLICK_ON_GROUP = "//p[normalize-space()='12345']"
NAZVANIE_SLOVARYA = "//input[@name='title']"



'''locators for check-lists'''
# inputs
INPUT_CHECK_LIST_NAME = "[name='title']"
# buttons
BUTTON_CHECK_LIST = "markup_nav_checklists"
BUTTON_DOBAVIT_CHECK_LIST = "markup_addChecklists"