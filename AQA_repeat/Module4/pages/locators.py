from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")


class BasketPageLocators:
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR,"div[class='basket-items']:nth-of-type(1) div[class='col-sm-1'] p")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='basket-items']:nth-of-type(1) h3 a:nth-child(1)")
