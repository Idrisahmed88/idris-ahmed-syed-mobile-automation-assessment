"""
BasePage: reusable UI actions shared by every screen.

Every action uses an *explicit* wait, so tests never rely on fixed sleeps and
are resilient to normal app load times. All page objects inherit from this.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except StaleElementReferenceException:
            self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self, locator, text):
        try:
            element = self.find(locator)
            element.clear()
            element.send_keys(text)
        except StaleElementReferenceException:
            element = self.find(locator)
            element.clear()
            element.send_keys(text)

    def text_of(self, locator):
        return self.find(locator).text

    def is_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
