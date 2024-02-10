import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class ElementActions:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        """Waits for an element to be clickable and then clicks it."""
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException as ex:
            logging.info(f"Exception has been thrown while waiting for element {locator} to be clickable: {str(ex)}")

    def get_element(self, locator):
        """Waits for an element to be visible and returns it."""
        try:
            return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        except TimeoutException as ex:
            logging.info(f"Exception has been thrown while waiting for element {locator} to be visible: {str(ex)}")
            return None
