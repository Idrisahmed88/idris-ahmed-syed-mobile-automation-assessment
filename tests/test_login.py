"""
Automated login tests.

TC-01 (valid login) is one of the two cases demonstrated in the coding video.
TC-02 is data-driven so several invalid combinations run from one test body.
"""
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

VALID_USER = "bod@example.com"
VALID_PASS = "10203040"
LOCKED_USER = "alice@example.com"


def test_valid_login_shows_catalog(driver):
    """TC-01: valid credentials log the user in and show the product catalog."""
    login = LoginPage(driver)
    login.open_login_screen().login(VALID_USER, VALID_PASS)
    products = ProductsPage(driver)
    assert products.catalog_is_displayed(), "Catalog not shown after valid login"


def test_locked_out_user_is_rejected(driver):
    """TC-02: the locked-out account is blocked with an account-locked error."""
    login = LoginPage(driver)
    login.open_login_screen().login(LOCKED_USER, VALID_PASS)
    assert login.locked_error_is_shown(), "Expected the account-locked error"
    products = ProductsPage(driver)
    assert not products.catalog_is_displayed(), "Locked user should not see catalog"
    login = LoginPage(driver)
    login.open_login_screen().login("alice@example.com", VALID_PASS)

    assert login.locked_error_is_shown(), "Expected the account-locked error"
