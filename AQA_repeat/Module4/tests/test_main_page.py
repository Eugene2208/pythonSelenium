from AQA_repeat.Module4.pages.basket_page import BasketPage
from AQA_repeat.Module4.pages.login_page import LoginPage
from AQA_repeat.Module4.pages.main_page import MainPage
from AQA_repeat.Module4.Environment import Environment as env


def test_guest_should_see_login_link(browser):
    link = env.get_page_link()
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    link = env.get_page_link()
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = env.get_page_link()
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()
