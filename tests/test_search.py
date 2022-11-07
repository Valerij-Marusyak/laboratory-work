import unittest
from selenium.webdriver.common.keys import Keys
from page_object.search_page import Search
from webdriver_factory import WebDriverFactory

class SearchPageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.search_page = Search(self.driver)
        self.search_page.open()
        pass

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')
        self.driver.quit()

    def test_apple(self) -> None:
        self.search_page.set_query('apple')
        self.search_page.click_search_button()

        name = self.search_page.get_name()
        self.assertEqual("Apple Cinema 30\"", name)

        price = self.search_page.get_price()
        self.assertEqual('110.00', price)

    def test_sony(self) -> None:
        self.search_page.set_query('sony')
        self.search_page.click_search_button()

        name = self.search_page.get_name()
        self.assertEqual("Sony VAIO", name)

        price = self.search_page.get_price()
        self.assertEqual('1202.00', price)

    def test_nokia(self) -> None:
        self.search_page.set_query('nokia')
        self.search_page.click_search_button()

        name = self.search_page.get_alert()
        self.assertEqual("There is no product that matches the search criteria.", name)

    def test_in_description(self) -> None:
        self.search_page.set_query('stunning')
        self.search_page.toggle_search_in_product_descriptions_checkbox()
        self.search_page.click_search_button()

        actual_result = self.search_page.get_search_results()
        self.assertEqual(['HP LP3065', 'iMac'], actual_result)
