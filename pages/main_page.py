from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
##Test Test

class MainPage(Page):
    SETTINGS = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
    ADD_PROJ = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")

    def open_settings(self):
        settings = WebDriverWait (self.driver,25).until(EC.element_to_be_clickable(self.SETTINGS))
        settings.click()

    def add_a_project(self):
        project = WebDriverWait (self.driver,25).until(EC.element_to_be_clickable(self.ADD_PROJ))
        project.click()

