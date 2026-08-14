from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "bod@example.com"
VALID_PASS = "10203040"


def test_place_order_end_to_end(driver):
    """TC-07: a logged-in user can complete checkout and place an order."""
    LoginPage(driver).open_login_screen().login(VALID_USER, VALID_PASS)
    products = ProductsPage(driver)
    products.open_first_product().add_to_cart()
    products.open_cart()
    CartPage(driver).proceed_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.fill_shipping("Idris Ahmed Syed", "123 Test Street", "Hyderabad", "500001", "India")
    checkout.fill_payment("Idris Ahmed Syed", "4111111111111111", "12/28", "123")
    checkout.place_order()
    assert checkout.order_is_confirmed(), "Order confirmation was not shown"
