import logging

import pages
from utils.element_actions import ElementActions

'''
This Python script provides functions for configuring and initializing an Appium driver for mobile app testing. It includes:
Configuration Loading: Loads testing settings from test_config.json, specifying Appium driver capabilities.
Driver Initialization: Creates and returns an Appium driver with settings derived from the loaded configuration, ready for automating tests on Android devices.
'''
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