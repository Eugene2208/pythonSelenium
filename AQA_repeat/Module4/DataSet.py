import string
from enum import Enum
import random


class PageLinks(Enum):
    product_page1 = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page2 = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


class ProductName(Enum):
    product_name1 = "The shellcoder's handbook"
    product_name2 = "Coders at Work"


class ProductPrice(Enum):
    product_name1_GBP = "9,99 £"
    product_name2_GBP = "19,99 £"


class Credential(Enum):
    email1 = ''.join(random.choice(string.ascii_letters) for i in range(10))+"@email.com"
    pass1 = "SomePass"
