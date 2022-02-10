from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_selected_product(self, name: str, price):
        self.should_be_product_name()
        self.should_be_product_price()
        f_name = self.browser.find_element(*BasketPageLocators.FIRST_PRODUCT_NAME).text
        f_price = self.browser.find_element(*BasketPageLocators.FIRST_PRODUCT_PRICE).text
        assert name == str(f_name), "Product name is wrong"
        assert f_price == str(price), "Product price is wrong"

    def should_be_product_name(self):
        assert self.is_element_present(*BasketPageLocators.FIRST_PRODUCT_NAME), "Product name not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*BasketPageLocators.FIRST_PRODUCT_PRICE), "Product price not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY_NOW), "There are items in the basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), "No message that basket is empty"