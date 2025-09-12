from uuid import uuid4
from user import User
from menu import MenuItem
from cart import Cart
from restaurant import Restaurant
from strategy import IPaymentStrategy


class Order:
    def __init__(self):
        self.id = uuid4()
        self.order_items = []
        self.user = None
        self.cart = None
        self.restaurant = None
        self.schedule = None
        self.payment_method = None
    
    def add_order_item(self, items : MenuItem):
        self.order_items = items

    def set_user(self, user : User):
        self.user = user
    
    def set_cart(self, cart : Cart):
        self.cart = cart
    
    def set_restaurant(self, restaurant : Restaurant):
        self.restaurant = restaurant
    
    def set_schedule(self, schedule):
        self.schedule = schedule
    
    def set_payment_method(self, method : IPaymentStrategy):
        self.payment_method = method
    
    def get_total(self):
        return self.cart.get_total()

class DeliveryOrder(Order):
    def __init__(self):
        super().__init__()
        self.address = None
    
    def set_delivery_address(self, address : str):
        self.address = address
    
    def get_type(self):
        return "Delivery"
    
class PickUpOrder(Order):
    def __init__(self):
        super().__init__()
        self.address = None
    
    def set_pickup_address(self, address : str):
        self.address = address

    def get_type(self):
        return "Pickup"

