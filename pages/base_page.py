import logging

import pages
from utils.element_actions import ElementActions

"""
This BasePage class serves as the foundation for all page objects within the framework,
centralizing common functionalities and properties.Integrates an action handler for performing actions like clicks and text inputs,
equipped to handle intermediate elements like pop-ups or modals dynamically encountered during tests.
The class provides a mechanism to update the web driver instance, ensuring actions are performed
using the current session's driver, facilitating seamless test execution across different pages.
"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        intermediate_elements_page = pages.IntermediateElementsPage()
        logging.info(f"Base Page driver session id {self.driver.session_id}")
        self.actions = ElementActions(self.driver, intermediate_elements_page)

    def set_driver(self, driver):
        self.driver = driver
        self.actions.driver = driver
        logging.info(f"Updated Base Page driver session id {self.driver.session_id}")