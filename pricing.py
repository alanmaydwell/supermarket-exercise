
def simple(quantity, unit_price):
    price = round(quantity * unit_price, 2)
    return price

def bogof(quantity, unit_price):
    if quantity > 1:
        if quantity%2 == 0:
            quantity = quantity * 0.5
        else:
            quantity = ((quantity-1) * 0.5) + 1 
    price = simple(quantity, unit_price)
    return price

def special_sr1(quantity, unit_price):
    if quantity >= 3:
        unit_price = 4.50
    price = simple(quantity, unit_price)
    return price
