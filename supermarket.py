
products = {"FR1": "Fruit tea",
            "SR1": "Strawberries",
            "CF1": "Coffee"}


class Checkout:
    def __init__(self):
        self.reset_basket()
        
    def reset_basket(self):
        self.items = {k:0 for k in products}

    def add_item(self, item_code, quantity=1):
        self.items[item_code] +=quantity
        
    def get_prices(self):
        pass
    
        
if __name__ == "__main__":
    basket = Checkout()
    basket.add_item("FR1")
    basket.add_item("SR1")
    basket.add_item("CF1")
    print(basket.items)
