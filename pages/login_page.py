from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Test Test

class LogInPage(Page):
    EMAIL = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    LOGIN = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(4)

    def login_page(self):
        email = WebDriverWait (self.driver,25).until(EC.presence_of_element_located(self.EMAIL))

        email.send_keys("tranglejenny@yahoo.com")

        password = WebDriverWait (self.driver,25).until(EC.presence_of_element_located(self.PASSWORD))

        password.send_keys("Victoria13")
        sleep(4)



        login = WebDriverWait (self.driver,20).until(EC.element_to_be_clickable(self.LOGIN))
        login.click()
