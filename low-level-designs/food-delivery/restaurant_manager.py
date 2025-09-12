import threading
from restaurant import Restaurant


class RestaurantManager(threading.Thread):
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
        self.restaurants = []
    
    def add_restaurant(self, restaurant : Restaurant):
        self.restaurants.append(restaurant)

    def list_restaurants(self):
        for restaurant in self.restaurants:
            print(f"Restauarnt name : {restaurant.name}, address : {restaurant.address}")
    
    def search_restaurant(self, location : str):
        result = []
        for restaurant in self.restaurants:
            if location == restaurant.address:
                result.append(restaurant)
        return result
