from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class NotificationsPage(BasePage):
    __done_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")
    __permission_deny_btn = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")

    def default_notifications_deny(self):
        self.actions.click(self.__done_btn)
        self.actions.click(self.__permission_deny_btn)
