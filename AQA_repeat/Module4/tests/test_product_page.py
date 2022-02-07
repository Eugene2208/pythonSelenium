import pytest

from AQA_repeat.Module4.Environment import Environment as env
from AQA_repeat.Module4.pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize('link', [f"{env.get_page_link()}/?promo=offer{no}" for no in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_add_to_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = env.get_page_link()
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = env.get_page_link()
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = env.get_page_link()
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.should_be_disappeared_success_message()
