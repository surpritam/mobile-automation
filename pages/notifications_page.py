from appium.webdriver.common.appiumby import AppiumBy

import pages

'''
Page elements and methods related to Notifications page
'''
class NotificationsPage(pages.BasePage):
    _done_btn = (AppiumBy.ID, "com.fivemobile.thescore:id/btn_primary")

    def default_notifications_deny(self):
        self.actions.click(self._done_btn)
