"""Page object for the cart and the entry to the checkout flow."""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("My Cart")')
    CART_ITEM_LABEL = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    ITEMS_COUNT = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/itemsTV")
    PROCEED_TO_CHECKOUT = (AppiumBy.ACCESSIBILITY_ID, "Confirms products for checkout")

    def has_items(self):
        return self.is_visible(self.CART_ITEM_LABEL)

    def item_name(self):
        return self.text_of(self.CART_ITEM_LABEL)

    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT)
        return self
