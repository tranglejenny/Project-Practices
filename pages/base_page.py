from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)
        #logger.info(f'Opening url {url}')

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        #logger.info(f'Clicking on {locator}')


    def find_element(self, *locator):
        #logger.info(f'Searching for element {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self,  *locator):
        #logger.info(f'Searching for elements {locator}')
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        #logger.info(f"Inputting for text '{text}' for element {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_new_window(self):
        self.driver.wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def close_page(self):
        self.driver.close()

    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)



    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message= f'Element by {locator} not clickable'
        ).click()

    def wait_for_element_appear(self, *locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Element by {locator} not apprea')
        return element

    def wait_for_element_disappear(self, *locator):
        element = self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'Element by {locator} still visible')

    def wait_for_element_visibility(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible')
        return element


    def wait_for_url_to_change(self, initial_url):
        element = self.wait.until(
            EC.url_changes(initial_url),
            message=f'url {initial_url} did not change')


    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f'Expected text {expected_text} not in actual text {actual_text}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Expected text {expected_text} not the same actual text {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in url')

