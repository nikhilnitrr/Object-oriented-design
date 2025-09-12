from abc import ABC, abstractmethod
from order import DeliveryOrder, PickUpOrder
from datetime import datetime
from cart import Cart
from user import User
from restaurant import Restaurant
from strategy import IPaymentStrategy


class IOrderFactory(ABC):
    @abstractmethod
    def create_order():
        pass


class NowOrderFactory(IOrderFactory):
    def create_order(
        self,
        type: str,
        items: list,
        cart: Cart,
        user: User,
        restaurant: Restaurant,
        payment_method: IPaymentStrategy,
    ):
        if type == "delivery":
            order = DeliveryOrder()
            order.set_delivery_address(user.address)
        elif type == "pickup":
            order = PickUpOrder()
            order.set_pickup_address(restaurant.address)
        else:
            raise Exception(err_msg="Invalid order type, cannot create order")
        order.add_order_item(items)
        order.set_cart(cart)
        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_payment_method(payment_method)
        order.set_schedule(datetime.now())
        return order
    
class ScheduleOrderFactory(IOrderFactory):
    def create_order(
        self,
        type: str,
        items: list,
        cart: Cart,
        user: User,
        restaurant: Restaurant,
        payment_method: IPaymentStrategy,
        schedule : str
    ):
        if type == "delivery":
            order = DeliveryOrder()
            order.set_delivery_address(user.address)
        elif type == "pickup":
            order = PickUpOrder()
            order.set_pickup_address(restaurant.address)
        else:
            raise Exception(err_msg="Invalid order type, cannot create order")
        order.add_order_item(items)
        order.set_cart(cart)
        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_payment_method(payment_method)
        order.set_schedule(schedule)
        return order
