from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
#Test Test
class SearchResultsPage (Page):
    INPUT_FIELDS = (By.CSS_SELECTOR, "[class*='input book']")
    SEND_APPLICATION = (By.CSS_SELECTOR, "[type = 'submit']")
    def verify_search_url(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)
        sleep(2)

    def input_fields(self):
        fields = self.find_elements(*self.INPUT_FIELDS)
        for i in range(len(fields)):
            self.find_elements(*self.INPUT_FIELDS)

    def send_application(self):
        application = WebDriverWait (self.driver,25).until(EC.element_to_be_clickable(self.SEND_APPLICATION))
        application.click()



