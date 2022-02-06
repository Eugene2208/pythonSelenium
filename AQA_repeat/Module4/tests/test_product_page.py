from AQA_repeat.Module4.DataSet import PageLinks, ProductName, ProductPrice
from AQA_repeat.Module4.pages.basket_page import BasketPage
from AQA_repeat.Module4.pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = PageLinks.product_page2.value
    prod_page = ProductPage(browser, link)
    prod_page.open()
    prod_page.add_to_basket()
    prod_page.solve_quiz_and_get_code()
    prod_page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_selected_product(ProductName.product_name2.value, ProductPrice.product_name2_GBP.value)
