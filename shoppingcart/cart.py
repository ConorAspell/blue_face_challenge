import typing

from . import abc
import json
from currency_conversion.currency import get_amount_in_currency


class ShoppingCart(abc.ShoppingCart):
    def __init__(self):
        self._items = dict()

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity
    '''
    This method prints out the items in the cart.
    It returns a list of dictionaries for each item in the cart.
    '''
    def print_receipt(self) -> typing.List[str]:
        lines = []
        total=0
        purchase = {}
        print("-" *39)
        print("|ITEM        | Quantity       | Price |")
        for item in self._items.items():
            price = self._get_product_price(item[0]) * item[1]
            total+=price
            price_string = "€%.2f" % price
            purchase['item'] = item[0]
            purchase['cost'] = price_string
            purchase['quantity'] = str(item[1])
            if price == 0:
                continue
            print("|" +item[0].ljust(12) + "| " + str(item[1]).ljust(15) + '| ' + price_string.ljust(6) + "|")
            lines.append(purchase.copy())
        print("-"*39)
        print("|Total Price: ".ljust(33) + "€%.2f" % total+ "|")
        print("-"*39)
        return lines
    '''
    This method returns all the prices of the products for sale in the shop as a dictionary
    '''
    def _get_product_price(self, product_code: str) -> float:
        with open("products/products.json") as f:
            p_dict = json.load(f)
        return p_dict.get(product_code, 0)
    
    '''
    This method returns all the prices of the products for sale in the shop in a chosen currency as a dictionary
    '''

    def display_product_list_in_currency(self, currency):
        with open("products/products.json") as f:
            p_dict = json.load(f)
        r_dict = {k:get_amount_in_currency(v, currency) for (k,v) in p_dict.items()}
        for k, v in r_dict.items():
            print(k + " : " + str(v))
        return r_dict
