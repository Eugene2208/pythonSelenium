from AQA_repeat.Module4.pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def add_to_basket(self):
        basket_btn = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        basket_btn.click()
