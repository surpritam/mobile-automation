from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Favorites teams page
'''
class FavoriteTeamsPage(pages.BasePage):
    _follow_favorite_default_first = (AppiumBy.XPATH, "(//android.widget.ImageView[@resource-id=\"com.fivemobile.thescore:id/follow_icon\"])[1]")
    _continue_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def choose_default_continue(self):
        self.actions.click(self._follow_favorite_default_first)
        self.actions.click(self._continue_btn)