from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from page_object.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Review(BasePage):

    def __init__(self, driver: WebDriver, product_id: str):
        super().__init__(driver)
        self.product_id = product_id

    def get_url(self) -> str:
        return f'http://54.183.112.233/index.php?route=product/product&product_id={self.product_id}'

    def tab_review(self) -> WebElement:
        review = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Reviews')
        return review

    def open_review_tab(self) -> None:
        self.tab_review().click()   # сделать явное ожидание

    def continue_button(self) -> WebElement:
        continue_button = self.driver.find_element(By.ID, 'button-review')
        return continue_button

    def click_continue(self) -> None:
        self.continue_button().click()

        WebDriverWait(self.driver, 10).until(
            EC.any_of(
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-danger')),
                EC.presence_of_element_located((By.CLASS_NAME, 'alert-success'))
            )
        )

    def warning(self) -> str:
        warning = self.driver.find_element(By.CLASS_NAME, 'alert-danger').text
        return warning

    def success(self) -> str:
        success = self.driver.find_element(By.CLASS_NAME, 'alert-success').text
        return success

    def get_rating_input(self, rating: int) -> WebElement:
        rating = self.driver.find_element(By.CSS_SELECTOR, f"input[value='{rating}'][name='rating']")
        return rating

    def set_rating(self, rating: int) -> None:
        self.get_rating_input(rating).click()   # сделать явное ожидание

    def field_your_name(self) -> WebElement:
        name = self.driver.find_element(By.ID, "input-name")
        return name

    def set_review_name(self, name: str) -> None:
        self.field_your_name().send_keys(name)

    def field_your_review(self) -> WebElement:
        search_review = self.driver.find_element(By.ID, "input-review")
        return search_review

    def set_review_text(self, text: str) -> None:
        self.field_your_review().clear()
        self.field_your_review().send_keys(text)
