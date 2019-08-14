from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    SEARCH_BUTTON = (By.XPATH, '//*[@class = "ico ico--search"]')
    SEARCH_BOX = (By.NAME, 'q')

class SearchResultsPageLocators(object):
    pass
