from restaurant import Restaurant
from menu import MenuItem

class Cart:
    def __init__(self):
        self.restaurant = None
        self.cart_items = []
    
    def add_to_cart(self, menu_item : MenuItem):
        self.cart_items.append(menu_item)
    
    def set_restaurant(self, restaurant : Restaurant):
        self.restaurant = restaurant
    
    def is_empty(self):
        return True if self.cart_items else False
    
    def clear(self):
        self.cart_items = []
        self.restaurant = None

    def get_total(self):
        total = 0
        for items in self.cart_items:
            total+= items.price
        return total