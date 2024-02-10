from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class NotificationsPage(BasePage):
    __done_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def default_notifications_deny(self):
        self.actions.click(self.__done_btn)
