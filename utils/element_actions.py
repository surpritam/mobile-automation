import logging
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class ElementActions:
    def __init__(self, driver, intermediate_elements_page):
        self.driver = driver
        self.intermediate_elements = intermediate_elements_page.locators

    def _perform_with_retry(self, operation, locator, max_attempts=3, *args, **kwargs):
        """
        Retries an operation on an element, handling intermediate elements if necessary.
        """
        last_exception = None
        for attempt in range(max_attempts):
            try:
                if attempt > 0:
                    # Handle intermediate elements before retrying
                    self.handle_intermediate_elements()
                return operation(locator, *args, **kwargs)
            except (TimeoutException, WebDriverException) as e:
                logging.info(f"Attempt {attempt + 1} failed for {locator}: {e}")
                last_exception = e
        raise last_exception  # Raise the last exception if all attempts fail

    def click(self, locator):
        """Waits for an element to be clickable and then clicks it, with retries."""
        logging.info(f"Click function session id: {self.driver.session_id}")
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc)).click()
        self._perform_with_retry(action, locator)

    def get_element(self, locator):
        """Waits for an element to be visible and returns it, with retries."""
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc))
        return self._perform_with_retry(action, locator)


    def send_keys(self, locator, send_text):
        """Sends text to the element"""
        action = lambda loc: WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(loc)).send_keys(send_text)
        self._perform_with_retry(action, locator)

    def handle_intermediate_elements(self):
        """Attempts to handle any intermediate elements based on the centralized list."""
        for locator in self.intermediate_elements:
            try:
                element = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(locator))
                element.click()
                # Tp Ensure the UI is stabilized and intermediate element no longer exists
                WebDriverWait(self.driver, 10).until_not(ec.visibility_of_element_located(locator))
            except TimeoutException:
                # If the intermediate element is not found or not clickable, assume it's not present and move on.
                continue
