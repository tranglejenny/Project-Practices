from pages.base_page import Page
from pages.search_results_page import SearchResultsPage
from pages.login_page import LogInPage
from pages.main_page import MainPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)

        self.search_results_page = SearchResultsPage(driver)
        self.main_page = MainPage(driver)
        self.login_page = LogInPage(driver)
