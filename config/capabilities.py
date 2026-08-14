"""
Central place for Appium capabilities and the server URL.

Values fall back to sensible defaults but can be overridden with environment
variables, so the same suite runs locally, in CI, or against a real device
without any code change (scalability / maintainability).
"""
import os

# Appium 2 server. Note the default base path is "/" (not "/wd/hub").
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")

# Path to the .apk. Download the Sauce Labs "My Demo App" APK and point here,
# or set APP_PATH in your environment / CI secrets.
APP_PATH = os.getenv("APP_PATH", "apps/Android-MyDemoApp.apk")


def android_capabilities() -> dict:
    """Return the UiAutomator2 capabilities for the target device."""
    return {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": os.getenv("DEVICE_NAME", "Android Emulator"),
        "appium:platformVersion": os.getenv("PLATFORM_VERSION", "13"),
        "appium:app": APP_PATH,
        # Reset app state between sessions so tests are independent.
        "appium:fullReset": False,
        "appium:noReset": False,
        "appium:newCommandTimeout": 120,
        "appium:autoGrantPermissions": True,
        "appium:androidInstallTimeout": 90000,
        "appium:appWaitActivity": "*",
    }
