import unittest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from page_object.shopping_cart_page import ShoppingCart
from page_object.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class ShoppingCartTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')
        self.driver.quit()

    def test_shopping_cart(self) -> None:
        samsung_product = ProductPage(self.driver, product_id="33")
        samsung_product.open()
        samsung_product.set_quantity('2')
        samsung_product.add_to_cart()
        alert_success = samsung_product.alert_success()
        self.assertEqual('Success: You have added Samsung SyncMaster 941BW to your shopping cart!', alert_success)

        hp_product = ProductPage(self.driver, product_id="47")
        hp_product.open()
        hp_product.set_quantity('1')
        hp_product.add_to_cart()
        alert_success = hp_product.alert_success()
        self.assertEqual('Success: You have added HP LP3065 to your shopping cart!', alert_success)

        shopping_cart = ShoppingCart(self.driver)
        shopping_cart.open_cart()
        list_products = shopping_cart.products()
        self.assertEqual(['Samsung SyncMaster 941BW', 'HP LP3065'], list_products)
        self.assertEqual("$606.00", shopping_cart.get_cart_total())

        shopping_cart.clear_cart()
        alert_empty = shopping_cart.alert_empty()
        self.assertEqual('Your shopping cart is empty!', alert_empty)
