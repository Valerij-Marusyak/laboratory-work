import unittest
from page_object.review_page import Review
from webdriver_factory import WebDriverFactory


class AddReviewTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = WebDriverFactory.get_driver()
        self.review_page = Review(self.driver, product_id="42")
        self.review_page.open()

    def tearDown(self) -> None:
        self.driver.save_screenshot("screenshots/" + self.id() + '.png')
        self.driver.quit()

    def test_empty_fields(self) -> None:
        self.review_page.open_review_tab()
        self.review_page.click_continue()

        warning = self.review_page.warning()
        self.assertEqual('Warning: Please select a review rating!', warning)

    def test_short_text(self) -> None:
        self.review_page.open_review_tab()
        self.review_page.set_rating(5)
        self.review_page.set_review_name("John")
        self.review_page.set_review_text("k" * 24)
        self.review_page.click_continue()

        warning = self.review_page.warning()
        self.assertEqual('Warning: Review Text must be between 25 and 1000 characters!', warning)

    def test_ok(self) -> None:
        self.review_page.open_review_tab()
        self.review_page.set_rating(5)
        self.review_page.set_review_name("John")
        self.review_page.set_review_text("k" * 27)
        self.review_page.click_continue()

        success = self.review_page.success()
        self.assertEqual('Thank you for your review. It has been submitted to the webmaster for approval.', success)
