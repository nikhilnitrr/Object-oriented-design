from abc import ABC, abstractmethod

# Interface for declaring a character
class Character(ABC):
    @abstractmethod
    def get_abilities(self):
        pass

# Concrete character
class Mario(Character):
    def get_abilities(self):
        return "Mario "

# CharacterDecorator "is-a" decorator and "has-a" decorator
# It is also an abstract class (did not override get_abilities())
class CharacterDecorator(Character):
    def __init__(self, character : Character):
        self.character = character

# Concrete decorators

# HeightUp decorator
class HeightUp(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_abilities(self):
        return self.character.get_abilities() + "with height up "

# PowerUp decorator
class PowerUp(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)
    
    def get_abilities(self):
        return self.character.get_abilities() + "with power up "

# StarPower decorator
class StarPower(CharacterDecorator):
    def __init__(self, character):
        super().__init__(character)

    def get_abilities(self):
        return self.character.get_abilities() + "with star power "
    

if __name__ == "__main__":
    mario = Mario()
    print(mario.get_abilities())

    mario = HeightUp(mario)
    print(mario.get_abilities())

    mario = PowerUp(mario)
    print(mario.get_abilities())

    mario = StarPower(mario)
    print(mario.get_abilities())