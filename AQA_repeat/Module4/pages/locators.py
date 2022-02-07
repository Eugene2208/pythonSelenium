from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[class='alertinner ']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a[class='btn btn-default']")


class BasketPageLocators:
    FIRST_PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='basket-items']:nth-of-type(1) div[class='col-sm-1'] p")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, "div[class='basket-items']:nth-of-type(1) h3 a:nth-child(1)")
