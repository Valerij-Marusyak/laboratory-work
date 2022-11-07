import unittest
from selenium.webdriver.remote.webdriver import WebDriver
from page_object.product_page import ProductPage
from webdriver_factory import WebDriverFactory


class ProductPageTest(unittest.TestCase):

    driver: WebDriver | None = None
    product: ProductPage | None = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = WebDriverFactory.get_driver()
        cls.product = ProductPage(cls.driver, '42')
        cls.product.open()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')

    def test_get_name(self) -> None:
        name = self.product.get_name()
        self.assertEqual("Apple Cinema 30\"", name)

    def test_get_brand(self) -> None:
        brand = self.product.get_brand()
        self.assertEqual("Apple", brand)

    def test_get_product_code(self) -> None:
        product_code = self.product.get_product_code()
        self.assertEqual("Product Code: Product 15", product_code)

    def test_get_price(self) -> None:
        product_price = self.product.get_price()
        self.assertEqual("$110.00", product_price)

    def test_get_description(self) -> None:
        product_description = self.product.get_description()
        self.assertIn('The 30-inch Apple Cinema HD Display delivers an amazing 2560 x 1600 pixel resolution.',
        product_description)
