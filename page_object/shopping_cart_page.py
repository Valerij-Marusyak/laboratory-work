from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from page_object.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCart(BasePage):

    def open_cart(self) -> None:
        self.driver.get('http://54.183.112.233/index.php?route=checkout/cart')

    def alert_empty(self) -> str:
        alert_empty = self.driver.find_element(By.ID, 'content').find_element(By.TAG_NAME, 'p').text
        return alert_empty

    def remove_buttons(self) -> list[WebElement]:
        remove_area = self.driver.find_element(By.ID, 'content')
        products_to_remove = remove_area.find_elements(By.CLASS_NAME, 'btn-danger')
        return products_to_remove

    def clear_cart(self) -> None:
        for _ in self.remove_buttons():
            remove_area = self.driver.find_element(By.ID, 'content')
            product = remove_area.find_element(By.CLASS_NAME, 'btn-danger')
            product.click()
            WebDriverWait(self.driver, 10).until(EC.staleness_of(product))

    def products(self) -> list[str]:
        result: list[str] = []
        products = self.driver.find_element(By.CLASS_NAME, 'table-responsive').find_elements(By.TAG_NAME, 'a')
        for product in products:
            if len(product.text) > 0:           #
                result.append(product.text)
        return result

    def get_cart_total(self) -> str:
        total = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/table/tbody/tr[4]/td[2]').text
        return total
