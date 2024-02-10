import pytest

from pages.intermediate_elements_page import IntermediateElementsPage
from utils.element_actions import ElementActions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        intermediate_elements_page = IntermediateElementsPage()
        self.actions = ElementActions(driver, intermediate_elements_page)
