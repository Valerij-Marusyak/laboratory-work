from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from page_object.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ComparePage(BasePage):

    def get_url(self) -> str:
        return 'http://54.183.112.233/index.php?route=product/compare'

    def list_products(self) -> list[str]:
        result = []
        products = self.driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'a')
        for product in products:
            result.append(product.text)
        return result

    def remove_products(self) -> None:
        remove_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn-danger')
        for _ in remove_buttons:
            remove_button = self.driver.find_element(By.CLASS_NAME, 'btn-danger')
            remove_button.click()
            WebDriverWait(self.driver, 10).until(EC.staleness_of(remove_button))

    def alert_text(self) -> str:
        text = self.driver.find_element(By.ID, 'content').find_element(By.TAG_NAME, 'p').text
        return text
