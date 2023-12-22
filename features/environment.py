from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
#Test Test Test Test


from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """



    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ###### Other Browser:
    # service = Service(executable_path="/Users/jle@sitetracker.com/QA/Project-Practice/geckodriver")
    # context.driver = webdriver.Firefox(service=service)



    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'jennyle_2L1kaj'
    # bs_key = 'Fy2pXEdxkdY4eTRXJdGX'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',
    #     'osVersion': '10',
    #     'browserName': 'Firefox',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    # comment





    context.driver.set_window_size(1280, 720)


    context.driver.wait = WebDriverWait(context.driver, 15)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    #logger.info(f'Started scenario:{scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    #logger.info(f'\nStarted step:{step.name}')


# def after_step(context, step):
#     if step.status == 'failed':
#         #context.driver.save_screenshot(f'{step}.png')
#         print('\nStep failed: ', step)
#         #logger.warning(f'Started step:{step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
