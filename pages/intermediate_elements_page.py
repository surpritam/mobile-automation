from appium.webdriver.common.appiumby import AppiumBy

'''
Page elements and methods related to Favorites league page
'''
class IntermediateElementsPage:
    def __init__(self):
        self.locators = [
            (AppiumBy.ID, "com.fivemobile.thescore:id/btn_disallow"),
            (AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button"),
            (AppiumBy.ID, "com.fivemobile.thescore:id/dismiss_modal"),
        ]
