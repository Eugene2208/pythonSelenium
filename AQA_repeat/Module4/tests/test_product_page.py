import pytest

from AQA_repeat.Module4.Environment import Environment as env
from AQA_repeat.Module4.pages.product_page import ProductPage


@pytest.mark.parametrize('link', [f"{env.get_page_links()}/?promo=offer{no}" for no in range(10)])
def test_guest_can_add_product_to_basket(browser, link):
    # link = env.get_page_links()
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.should_be_add_to_basket()
