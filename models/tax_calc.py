from math import ceil  
def round_up_to_005(n):
    return ceil(n*20) / 20


def tax_calculator(product):

    withdrawn_tax = 0
    basic_tax = 0
    # check if product is exempted from tax
    if product.exempt == False:
        # calc basic tax if not exception
        basic_tax = round_up_to_005((10*product.price)/100)
        withdrawn_tax += basic_tax
    # check if imported or not
    if product.imported:
        new_price = basic_tax + product.price
        import_tax = round_up_to_005((5*product.price)/100)
        price_tax = round(new_price + import_tax, 2)
        withdrawn_tax += import_tax

        return price_tax, withdrawn_tax
    else:
        price_tax = round(product.price + basic_tax, 2)
        return price_tax, withdrawn_tax


