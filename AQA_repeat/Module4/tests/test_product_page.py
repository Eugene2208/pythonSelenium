import pytest

from AQA_repeat.Module4.DataSet import Credential
from AQA_repeat.Module4.Environment import Environment as env
from AQA_repeat.Module4.pages.basket_page import BasketPage
from AQA_repeat.Module4.pages.login_page import LoginPage
from AQA_repeat.Module4.pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.mark.need_review
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = env.get_page_link()
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = env.get_page_link()
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = env.get_page_link()
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()
        login_page.register_new_user(Credential.email1.value, Credential.pass1.value)
        login_page.should_be_authorized_user()

    @pytest.mark.skip
    @pytest.mark.need_review
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = env.get_page_link()
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.add_to_basket()
        prod_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = env.get_page_link()
        prod_page = ProductPage(browser, link)
        prod_page.open()
        prod_page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('link', [f"{env.get_page_link()}/?promo=offer{no}" for no in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_add_to_basket()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = env.get_page_link()
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_be_disappeared_success_message()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = env.get_page_link()
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()
