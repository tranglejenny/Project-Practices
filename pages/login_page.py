from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class LogInPage(Page):
    EMAIL = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    LOGIN = (By.CSS_SELECTOR, '[wized="loginButton"]')

    def open_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(2)

    def login_page(self):
        email = self.wait_for_element_appear(*self.EMAIL)

        email.send_keys("tranglejenny@yahoo.com")

        password = self.wait_for_element_appear(*self.PASSWORD)

        password.send_keys("Victoria13")


        sleep(2)
        login = self.wait_for_element_click(*self.LOGIN)