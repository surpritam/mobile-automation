from appium.webdriver.common.appiumby import AppiumBy

import pages


class SearchPage(pages.BasePage):
    __search_txt = (AppiumBy.ID,"com.fivemobile.thescore:id/search_src_text")

    def search(self, search_text):
        self.actions.send_keys(self.__search_txt,search_text)