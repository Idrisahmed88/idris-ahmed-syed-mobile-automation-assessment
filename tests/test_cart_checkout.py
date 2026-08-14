"""
Automated cart & checkout tests.

TC-04 (add to cart) is the second case demonstrated in the coding video.
"""
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_add_product_to_cart(driver):
    """TC-04: adding a product places it in the cart."""
    products = ProductsPage(driver)
    products.open_first_product().add_to_cart()
    products.open_cart()
    cart = CartPage(driver)
    assert cart.has_items(), "Added product not present in the cart"
