from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FULL_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/fullNameET")
    ADDRESS_1 = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/address1ET")
    CITY = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cityET")
    ZIP = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/zipET")
    COUNTRY = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/countryET")
    TO_PAYMENT_BTN = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    CARD_NAME = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    CARD_NUMBER = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cardNumberET")
    CARD_EXPIRY = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/expirationDateET")
    CARD_CVV = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/securityCodeET")
    REVIEW_BTN = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    PLACE_ORDER_BTN = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    CONFIRMATION = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Checkout Complete")')

    def fill_shipping(self, name, address, city, zip_code, country):
        self.type(self.FULL_NAME, name)
        self.type(self.ADDRESS_1, address)
        self.type(self.CITY, city)
        self.type(self.ZIP, zip_code)
        self.type(self.COUNTRY, country)
        self.click(self.TO_PAYMENT_BTN)
        return self

    def fill_payment(self, name, number, expiry, cvv):
        self.type(self.CARD_NAME, name)
        self.type(self.CARD_NUMBER, number)
        self.type(self.CARD_EXPIRY, expiry)
        self.type(self.CARD_CVV, cvv)
        self.click(self.REVIEW_BTN)
        return self

    def place_order(self):
        self.click(self.PLACE_ORDER_BTN)
        return self

    def order_is_confirmed(self):
        return self.is_visible(self.CONFIRMATION)
