from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from page_object.base_page import BasePage
from page_object.text_tools import extract_price

class Search(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/search'

    def search_field(self) -> WebElement:
        search_field = self.driver.find_element(By.ID, 'input-search')
        return search_field

    def set_query(self, name: str) -> None:
        search_field = self.search_field()
        search_field.clear()
        search_field.send_keys(name)

    def toggle_search_in_product_descriptions_checkbox(self) -> None:
        self.search_in_product_descriptions_checkbox().click()
        # сделать явное ожидание

    def search_in_product_descriptions_checkbox(self) -> WebElement:
        checkbox = self.driver.find_element(By.ID, 'description')
        return checkbox

    def click_search_button(self) -> None:
        self.search_button().click()
        # сделать явное ожидание

    def search_button(self) -> WebElement:
        search_button = self.driver.find_element(By.ID, 'button-search')
        return search_button

    def get_name(self) -> str:
        name = self.driver.find_element(By.CLASS_NAME, "caption")
        name = name.text.split('\n')[0]
        return name

    def get_price(self) -> str:
        price = self.driver.find_element(By.CLASS_NAME, 'price').text
        price = extract_price(price)
        return price

    def get_alert(self) -> str:
        name = self.driver.find_element(By.XPATH, '//*[@id="content"]/p[2]').text
        return name

    def get_search_results(self) -> list[str]:
        product_tags = self.driver.find_elements(By.CLASS_NAME, 'caption')
        products: list[str] = []
        for product_tag in product_tags:
            name: str = product_tag.find_element(By.TAG_NAME, 'h4').text
            products.append(name)
        return products
