import logging

import pytest

from pages.intermediate_elements_page import IntermediateElementsPage
from utils.element_actions import ElementActions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        intermediate_elements_page = IntermediateElementsPage()
        logging.info(f"Base Page driver session id {self.driver.session_id}")
        self.actions = ElementActions(self.driver, intermediate_elements_page)

    def set_driver(self, driver):
        self.driver = driver
        self.actions.driver = driver
        logging.info(f"Updated Base Page driver session id {self.driver.session_id}")