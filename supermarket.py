import pricing

products = {"FR1": "Fruit tea",
            "SR1": "Strawberries",
            "CF1": "Coffee"}

product_price_params = {"FR1": [3.11, pricing.bogof],
                        "SR1": [5.00, pricing.special_sr1],
                        "CF1": [11.23, pricing.simple]}


class Checkout:
    def __init__(self):
        self.reset_basket()
        
    def reset_basket(self):
        self.items = {k:0 for k in products}

    def add_item(self, item_code, quantity=1):
        self.items[item_code] += quantity
        
    def get_prices(self):
        total = 0.0
        for product_code, quantity in self.items.items():
            unit_price, price_function = product_price_params[product_code]
            item_price = price_function(quantity, unit_price)
            print(f"Code:{product_code} Quantity:{quantity} price:{item_price}")
            total += item_price
        print("Total:", total)
            
    
if __name__ == "__main__":
    basket = Checkout()
    basket.add_item("FR1")
    basket.add_item("SR1")
    basket.add_item("CF1")
    basket.get_prices()
    basket.add_item("FR1", 3)
    basket.get_prices()
    
