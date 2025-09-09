from abc import ABC, abstractmethod

# Burger interface
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Pizza interface
class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass

# Concrete implementations of burger
class BasicBurger(Burger):
    def prepare(self):
        return "Preparing basic burger"
    
class PremiumBurger(Burger):
    def prepare(self):
        return "Preparing premium burger"

class BasicWheatBurger(Burger):
    def prepare(self):
        return "Preparing basic wheat burger"
    
class PremiumWheatBurger(Burger):
    def prepare(self):
        return "Preparing premium wheat burger"

  
# Concrete implementations of pizza
class BasicPizza(Pizza):
    def prepare(self):
        return "Preparing basic pizza"
    
class PremiumPizza(Pizza):
    def prepare(self):
        return "Preparing premium pizza"

class BasicWheatPizza(Pizza):
    def prepare(self):
        return "Preparing basic wheat pizza"
    
class PremiumWheatPizza(Pizza):
    def prepare(self):
        return "Preparing premium wheat pizza"

# Abstract factory class
class MealFactory(ABC):
    @abstractmethod
    def create_burger(self):
        pass

    @abstractmethod
    def create_pizza(self):
        pass

# Concrete factory classes
class NormalMealFactory(MealFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicBurger()
        elif type == "premium":
            return PremiumBurger()
        else:
            return None
    
    def create_pizza(self, type):
        if type == "basic":
            return BasicPizza()
        elif type == "premium":
            return PremiumPizza()
        else:
            return None

class WheatMealFactory(MealFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicWheatBurger()
        elif type == "premium":
            return PremiumWheatBurger()
        else:
            return None
    
    def create_pizza(self, type):
        if type == "basic":
            return BasicWheatPizza()
        elif type == "premium":
            return PremiumWheatPizza()
        else:
            return None

if __name__ == "__main__":
    type = "premium"
    my_burger_1 = NormalMealFactory().create_burger(type)
    my_burger_2 = WheatMealFactory().create_burger(type)

    my_pizza_1 = NormalMealFactory().create_pizza(type)
    my_pizza_2 = WheatMealFactory().create_pizza(type)

    print(my_burger_1.prepare())
    print(my_burger_2.prepare())

    print(my_pizza_1.prepare())
    print(my_pizza_2.prepare())
