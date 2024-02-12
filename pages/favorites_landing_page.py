from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Favorites landing page
'''
class FavoritesLandingPage(pages.BasePage):
    _search_text_view = (AppiumBy.ID, "com.fivemobile.thescore:id/search_bar_text_view")


    def default_text_search_view(self) -> str:
        return self.actions.get_element(self._search_text_view).text

    def enter_text_search_view(self):
        self.actions.click(self._search_text_view)