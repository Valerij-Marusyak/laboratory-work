import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from laboratory_work.page_object.compare_page import ComparePage
from laboratory_work.page_object.product_page import ProductPage
from webdriver_factory import WebDriverFactory

class ComparePageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')
        self.driver.quit()

    def test_compare(self) -> None:
        apple_product = ProductPage(self.driver, product_id="42")
        apple_product.open()
        apple_product.add_to_compare()
        alert_success = apple_product.alert_success()
        self.assertEqual('Success: You have added Apple Cinema 30" to your product comparison!', alert_success)

        samsung_product = ProductPage(self.driver, product_id="33")
        samsung_product.open()
        samsung_product.add_to_compare()
        samsung_product.click_product_comparison()

        compare_page = ComparePage(self.driver)
        actual_result = compare_page.list_products()
        self.assertEqual(['Apple Cinema 30"', 'Samsung SyncMaster 941BW'], actual_result)

        compare_page.remove_products()
        alert_not_chosen = compare_page.alert_text()
        self.assertEqual('You have not chosen any products to compare.', alert_not_chosen)
