from element import BasePageElement
from locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class SearchTextElement(BasePageElement):
    locator = 'q'

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        print(f'Title is {self.driver.title}')
        return "Buty i odzież online w ZALANDO." in self.driver.title

    def click_search_button(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        element.click

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_enter(self):
        element = self.driver.find_element(*MainPageLocators.SEARCH_BOX)
        element.send_keys(Keys.ENTER)


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found" not in self.driver.page_source
