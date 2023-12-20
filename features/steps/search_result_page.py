from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from behave import given, when, then

@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)

@then('Verify input fields')
def input_fields (context):
    context.app.search_results_page.input_fields()

@then('Verify “Send an application” button is available and clickable')
def send_application(context):
    context.app.search_results_page.send_application()
