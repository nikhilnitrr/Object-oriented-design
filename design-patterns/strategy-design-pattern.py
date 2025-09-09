from abc import ABC, abstractmethod

# Interfaces declaring different Strategies
class Talkable(ABC):
    @abstractmethod
    def talk(self):
        raise NotImplementedError
    
class Walkable(ABC):
    @abstractmethod
    def walk(self):
        raise NotImplementedError

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError
    
class Apperable(ABC):
    @abstractmethod
    def appearance(self):
        raise NotImplementedError
    
# Concrete implementation of these strategies
class NoTalk(Talkable):
    def talk(self):
        print("I cannot talk")

class CanTalk(Talkable):
    def talk(self):
        print("I can talk")

class NoWalk(Walkable):
    def walk(self):
        print("I cannot walk")

class CanWalk(Walkable):
    def walk(self):
        print("I can walk")

class NoFly(Flyable):
    def fly(self):
        print("I cannot fly")

class CanFly(Flyable):
    def fly(self):
        print("I can fly")

class NoApperance(Apperable):
    def appearance(self):
        print("I donot appear")

class CanAppear(Apperable):
    def appearance(self):
        print("I can appear")

# Define the client (in this case creature)
class Creature:
    def __init__(self, t : Talkable, w : Walkable, f : Flyable, a : Apperable):
        self.talkable = t
        self.walkable = w
        self.flyable = f
        self.apperable = a
    
    def walk(self):
        self.walkable.walk()
    
    def talk(self):
        self.talkable.talk()

    def fly(self):
        self.flyable.fly()

    def appearance(self):
        self.apperable.appearance()

if __name__ == "__main__":
    human = Creature(CanTalk(), CanWalk(), NoFly(), CanAppear())
    human.talk()
    human.walk()
    human.fly()
    human.appearance()

    bacteria = Creature(NoTalk(), CanWalk(), NoFly(), NoApperance())
    bacteria.talk()
    bacteria.walk()
    bacteria.fly()
    bacteria.appearance()
