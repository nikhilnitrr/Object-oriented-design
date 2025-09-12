from abc import ABC, abstractmethod

class IPaymentStrategy(ABC):
    @abstractmethod
    def pay():
        pass

class UPIPayment(IPaymentStrategy):
    def pay(self):
        return "Paid using UPI"

class CardPayment(IPaymentStrategy):
    def pay(self):
        return "Paid using credit card"