from selenium import webdriver
import unittest
import page

class PageSearch(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\andrejew\PycharmProjects\chromedriver')
        base_url = 'https://www.zalando.pl'
        self.driver.get(base_url)

    def test_search_in_booking_com(self):
        """
        zalando.com search feature. Search for surfing clothes
        """

        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "python.org title doesn't match."
        main_page.search_text_element = "billabong"
        main_page.click_enter()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()

