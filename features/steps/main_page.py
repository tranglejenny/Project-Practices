import time

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SETTINGS = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
ADD_PROJ = (By.XPATH, "//div[@class='setting-text' and text()='Add a project']")


@then('Click on settings option')
def open_settings(context):
    context.app.main_page.open_settings()
@then('Click on Add a project')
def add_a_project(context):
    context.app.main_page.add_a_project()


