from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class FavoritesLandingPage(BasePage):
    #__dismiss_modal = (AppiumBy.ID, "com.fivemobile.thescore:id/dismiss_modal")
    __search_text_view = (AppiumBy.ID, "com.fivemobile.thescore:id/search_bar_text_view")

    def __handle_modal(self):
        self.actions.click(self.__dismiss_modal)

    def default_text_search_view(self) -> str:
        #self.__handle_modal()
        return self.actions.get_element(self.__search_text_view).text