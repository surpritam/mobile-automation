from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class InitialPage(BasePage):
    # Define locators
    __get_started_button = (AppiumBy.ID, "com.fivemobile.thescore:id/action_button_text")

    def navigate_initial_setup(self):
        self.actions.click(self.__get_started_button)