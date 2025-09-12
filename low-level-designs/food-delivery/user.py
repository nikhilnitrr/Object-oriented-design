from uuid import uuid4
from cart import Cart

class User:
    def __init__(self, name, address):
        self.id = uuid4()
        self.name = name
        self.address = address
        self.cart = None
    
    def set_cart(self, cart : Cart):
        self.cart = cart