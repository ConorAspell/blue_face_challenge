from currency_converter import CurrencyConverter

'''
This returns the conversion into the desired currency
It uses a library
'''
def get_amount_in_currency(amount : int, currency : str):
    c = CurrencyConverter()
    if currency in c.currencies:
        return round(c.convert(amount, 'EUR', currency), 2)
    else:
        return "Invalid Currency"