from AQA_repeat.Module4.DataSet import PageLinks, ProductName, ProductPrice


class Environment:
    @staticmethod
    def get_page_links():
        return PageLinks.product_page2.value

    @staticmethod
    def get_product_name():
        return ProductName.product_name2.value

    @staticmethod
    def get_product_price():
        return ProductPrice.product_name2_GBP.value
