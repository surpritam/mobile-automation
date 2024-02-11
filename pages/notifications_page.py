from appium.webdriver.common.appiumby import AppiumBy

import pages


class NotificationsPage(pages.BasePage):
    __done_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def default_notifications_deny(self):
        self.actions.click(self.__done_btn)
