from abc import ABC, abstractmethod

# Interface
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Concrete classes representing normal burgers
class BasicBurger(Burger):
    def prepare(self):
        return "Preparing Basic burger"

class PremiumBurger(Burger):
    def prepare(self):
        return "Preparing Premium burger"

class BasicWheatBurger(Burger):
    def prepare(self):
        return "Preparing basic wheat burger"

class PremiumWheatBurger(Burger):
    def prepare(self):
        return "Preparing premium wheat burger"

# Burger factory interface
class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self):
        pass

# Concrete burger factories
class NormalBurgerFactory(BurgerFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicBurger()
        elif type == "premium":
            return PremiumBurger()
        else:
            return None

class WheatBurgerFactory(BurgerFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicWheatBurger()
        elif type == "premium":
            return PremiumWheatBurger()
        else:
            return None

if __name__ == "__main__":
    type = "basic"
    my_burger_1 = NormalBurgerFactory().create_burger(type)
    my_burger_2 = WheatBurgerFactory().create_burger(type)

    print(my_burger_1.prepare())
    print(my_burger_2.prepare())