from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, driver: WebDriver, product_id: str):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'http://54.183.112.233/index.php?route=product/product&product_id={self.product_id}'

    def get_name(self) -> str:
        name = self.driver.find_element(By.TAG_NAME, 'h1').text
        return name

    def get_brand(self) -> str:
        brand = self.driver.find_element(By.LINK_TEXT, 'Apple').text
        return brand

    def get_product_code(self) -> str:
        product_code = self.driver.find_element(By.XPATH,
                                                '//*[@id="content"]/div[1]/div[2]/ul[1]/li[2]').text
        return product_code

    def get_price(self) -> str:
        product_price = self.driver.find_element(By.ID, 'content').find_elements(By.TAG_NAME, 'h2')
        product_price = product_price[1].text
        return product_price

    def get_description(self) -> str:
        product_description = self.driver.find_element(By.ID, 'tab-description').text
        return product_description

    def add_to_compare(self) -> None:
        self.compare_button().click()
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-success')))

    def compare_button(self) -> WebElement:
        compare_button = self.driver.find_element(By.CSS_SELECTOR, '[data-original-title="Compare this Product"]')
        return compare_button

    def alert_success(self) -> str:
        alert_success = self.driver.find_element(By.CLASS_NAME, 'alert-success')
        alert_success = alert_success.text.split('\n')[0]
        return alert_success

    def click_product_comparison(self) -> None:
        alert_comparison = self.driver.find_element(By.LINK_TEXT, 'product comparison')
        alert_comparison.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Product Comparison')))

    def qty_field(self) -> WebElement:
        qty_field = self.driver.find_element(By.ID, 'input-quantity')
        return qty_field

    def add_button(self) -> WebElement:
        add_button = self.driver.find_element(By.ID, 'button-cart')
        return add_button

    def set_quantity(self, quantity: str):
        qty_field = self.qty_field()
        qty_field.clear()
        qty_field.send_keys(quantity)

    def add_to_cart(self) -> None:
        add_button = self.add_button()
        add_button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'alert-success')))
