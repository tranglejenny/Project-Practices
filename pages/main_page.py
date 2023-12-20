from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class MainPage(Page):
    SETTINGS = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
    ADD_PROJ = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")

    def open_settings(self):
        self.driver.find_element(*self.SETTINGS).click()
        sleep(2)

    def add_a_project(self):
        self.driver.find_element(*self.ADD_PROJ).click()
        sleep(2)

