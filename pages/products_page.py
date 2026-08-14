"""Page object for the product catalog and product detail screens."""
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductsPage(BasePage):
    CATALOG_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/productTV")
    PRODUCT_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Product Image")
    ADD_TO_CART_BUTTON = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    CART_TAB = (AppiumBy.ACCESSIBILITY_ID, "View cart")
    CART_BADGE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/cartIV")

    def catalog_is_displayed(self):
        return self.is_visible(self.CATALOG_TITLE)

    def open_first_product(self):
        self.click(self.PRODUCT_ITEM)
        return self

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        return self

    def open_cart(self):
        self.click(self.CART_TAB)
        return self
