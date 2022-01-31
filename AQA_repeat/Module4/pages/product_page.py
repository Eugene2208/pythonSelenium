from selenium.common.exceptions import NoSuchElementException

from AQA_repeat.Module4.pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            basket_btn = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            basket_btn.click()
        except NoSuchElementException:
            assert False, "Add to Basket button is not presented"
