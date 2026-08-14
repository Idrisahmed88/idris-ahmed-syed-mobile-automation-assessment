"""
Page object for the login screen.

IMPORTANT: The accessibility IDs below match the Sauce Labs My Demo App (RN).
Always confirm them against your build using Appium Inspector — if a build
differs, changing the locator here is the only edit needed (that is the whole
point of the Page Object Model).
"""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LoginPage(BasePage):
    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    LOGIN_MENU_ITEM = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Log In")')
    USERNAME_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    PASSWORD_FIELD = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    LOGIN_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
    GENERIC_ERROR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("not match")')
    LOCKED_ERROR = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("locked out")')

    def open_login_screen(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGIN_MENU_ITEM)
        return self

    def login(self, username, password):
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def error_is_shown(self):
        return self.is_visible(self.GENERIC_ERROR)

    def locked_error_is_shown(self):
        return self.is_visible(self.LOCKED_ERROR)
