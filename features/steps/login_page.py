import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

EMAIL = (By.CSS_SELECTOR, "[type='email']")
PASSWORD = (By.CSS_SELECTOR, "[type='password']")
LOGIN = (By.CSS_SELECTOR, '[wized="loginButton"]')


@given('Open the main page')
def open_page(context):
    context.app.login_page.open_page()

@when('Log in to the page')
def login_page(context):
    context.app.login_page.login_page()


