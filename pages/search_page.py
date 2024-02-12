from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Search page
'''
class SearchPage(pages.BasePage):
    _search_txt = (AppiumBy.ID,"com.fivemobile.thescore:id/search_src_text")

    def search(self, search_text):
        self.actions.send_keys(self._search_txt,search_text)