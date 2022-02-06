from AQA_repeat.Module4.pages.base_page import BasePage
from AQA_repeat.Module4.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def should_be_add_to_basket(self):
        self.should_be_message()
        self.should_be_right_price()

    def should_be_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_MESSAGE).text
        assert message == product_name, f"{product_name} is not {message}"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, f"{product_price} not equal {basket_price}"

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        login_link.click()
