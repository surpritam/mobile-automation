from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to common navigation elements
'''
class NavigationPages(pages.BasePage):
    _navigate_up = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc=\"Navigate up\"]")

    def navigate_back(self):
        self.actions.click(self._navigate_up)