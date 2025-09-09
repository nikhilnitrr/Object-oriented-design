from abc import ABC , abstractmethod

# Burger interface
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

class BasicBurger(Burger):
    def prepare(self):
        return "Preparing Basic burger"
    
class StandardBurger(Burger):
    def prepare(self):
        return "Preparing Standard burger"
    
class PremiumBurger(Burger):
    def prepare(self):
        return "Preparing Premium burger"


# Factory class
class BurgerFactory:
    def createBurger(self, type):
        if type == "basic":
            return BasicBurger()
        elif type == "standard":
            return StandardBurger()
        elif type == "premium":
            return PremiumBurger()
        else:
            return None

if __name__ == "__main__":
    type = "standard"
    my_burger = BurgerFactory().createBurger(type)
    print(my_burger.prepare())