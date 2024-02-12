from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Favorites league page
'''
class FavoriteLeaguePage(pages.BasePage):
    _continue_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def continue_without_selecting(self):
        self.actions.click(self._continue_btn)