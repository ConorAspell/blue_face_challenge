from shoppingcart.cart import ShoppingCart
import json
from currency_conversion.currency import get_amount_in_currency
import sys

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 1)
    receipt = cart.print_receipt()
    assert receipt[0]['item'] == "apple"
    assert receipt[0]['quantity'] == "1"
    assert receipt[0]['cost'] == "€1.10"

def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("apple", 2)
    receipt = cart.print_receipt()
    assert receipt[0]['item'] == "apple"
    assert receipt[0]['quantity'] == "2"
    assert receipt[0]['cost'] == "€2.20"


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1)
    cart.add_item("kiwi", 1)
    receipt = cart.print_receipt()
    assert receipt[0]['item'] == "apple"
    assert receipt[0]['quantity'] == "1"
    assert receipt[0]['cost'] == "€1.10"
    assert receipt[1]['item'] == "kiwi"
    assert receipt[1]['quantity'] == "1"
    assert receipt[1]['cost'] == "€1.30"

def test_order():
    cart = ShoppingCart()
    cart.add_item("banana", 1)
    cart.add_item("kiwi", 1)
    cart.add_item("apple", 1)
    receipt = cart.print_receipt()
    assert receipt[0]['item'] == "banana"
    assert receipt[1]['item'] == "kiwi"
    assert receipt[2]['item'] == "apple"

def test_print_receipt(capsys):
    cart = ShoppingCart()
    
    cart.add_item("banana", 1)

    receipt = cart.print_receipt()
    out, err = capsys.readouterr()
    sys.stdout.write(out)
    sys.stderr.write(err)
    assert out.split('\n')[0] == "-"*39
    assert out.split('\n')[1] == "|ITEM        | Quantity       | Price |"
    assert out.split('\n')[2] == "|banana      | 1              | €1.60 |"
    assert out.split('\n')[3] == "-"*39
    assert out.split('\n')[4] == "|Total Price:                    €1.60|"
    assert out.split('\n')[5] == "-"*39

def test_currency():
    cart = ShoppingCart()
    r_dict=cart.display_product_list_in_currency('GBP')
    with open("products/products.json") as f:
        p_dict = json.load(f)
    ans1 = r_dict['apple']
    ans2 = get_amount_in_currency(p_dict['apple'], 'GBP')
    assert ans1 == ans2

