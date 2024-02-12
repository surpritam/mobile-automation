from appium.webdriver.common.appiumby import AppiumBy

import pages
'''
Page elements and methods related to Initial Get Started page
'''
class InitialPage(pages.BasePage):
    # Define locators
    _get_started_button = (AppiumBy.ID, "com.fivemobile.thescore:id/action_button_text")

    def navigate_initial_setup(self):
        self.actions.click(self._get_started_button)
