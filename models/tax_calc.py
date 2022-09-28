from math import ceil  
def round_up_to_005(n):
    return ceil(n*20) / 20


def tax_calculator(product):
    """
    summry: 
        calculate tax of the product
    

    Args:
        product (class): the product which the tax will be calculated from 

    Returns:
        price_tax: the price of the item after tax
        withdrawn_tax: withdrawn taax from the item
    """

    withdrawn_tax = 0
    basic_tax = 0
    # check if the product is exempted from tax
    # exempted? exempted = true ;)
    if product.exempt == False:
        # calc basic tax if not exception
        basic_tax = round_up_to_005((10*product.price)/100)
        withdrawn_tax += basic_tax
    # check if the imported or not
    if product.imported:
        new_price = basic_tax + product.price
        import_tax = round_up_to_005((5*product.price)/100)
        price_tax = round(new_price + import_tax, 2)
        withdrawn_tax += import_tax

        return price_tax, withdrawn_tax
    else:
        price_tax = round(product.price + basic_tax, 2)
        return price_tax, withdrawn_tax



def reciept(items):
    """
    summry: 
        a method that prints out the reciept, the new price of item, the total widthrawn tax and the total of the shopped items

    Args:
        items (list): list of the shopped items

    Returns:
        totaltax: rounded amount of the total withdrawn tax
        totalPrice: rounded amount of the total price
    """
    tax =None
    totaltax =0
    newTaxedItemPrice =None
    totalPrice =0
    for item in items:
        
        newTaxedItemPrice, tax = tax_calculator(item)
        print("******** The reciept ********")
        print(f"{item.amount} {item.get_Name()} {newTaxedItemPrice}")
        totaltax +=tax
        totalPrice += newTaxedItemPrice
    print(f"Sales Taxes: {round(totaltax,2)} \nTotal Price: {round(totalPrice,2)}")
    return round(totaltax,2), round(totalPrice,2)


def reciept_without_print(items):
    tax =None
    totaltax =0
    newTaxedItemPrice =None
    totalPrice =0
    for item in items:
        
        newTaxedItemPrice, tax = tax_calculator(item)
        totaltax +=tax
        totalPrice += newTaxedItemPrice
    return round(totaltax,2), round(totalPrice,2)


