"""
pytest fixtures shared across the test suite.

A fresh Appium session is created per test function so tests stay independent
and can run in any order (or in parallel).
"""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

from config.capabilities import APPIUM_SERVER_URL, android_capabilities


@pytest.fixture()
def driver():
    """Start an Appium session, hand it to the test, then always quit it."""
    options = UiAutomator2Options().load_capabilities(android_capabilities())
    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    driver.implicitly_wait(0)  # we rely on explicit waits only (predictable)
    yield driver
    driver.quit()
