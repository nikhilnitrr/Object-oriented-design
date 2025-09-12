import threading
from order import Order

class OrderManager(threading.Thread):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        super().__init__()
        self.orders = []
    
    def add_order(self, order : Order):
        self.orders.append(order)
    
    def list_orders(self):
        for order in self.orders:
            print(f"Order by {order.user.name}")
            print(f"Order from Restaurant {order.restaurant.address}")
            print(f"Order worth {order.get_total()}")
