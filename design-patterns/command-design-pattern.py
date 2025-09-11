from abc import ABC, abstractmethod

# Appliances
class Light:
    def on(self):
        print("Light turned on")
    
    def off(self):
        print("Light turned off")

class Fan:
    def on(self):
        print("Fan turned on")
    
    def off(self):
        print("Fan turned off")

# Command interface
class ICommand(ABC):
    @abstractmethod
    def do(self):
        raise NotImplementedError
    
    @abstractmethod
    def undo(self):
        raise NotImplementedError

# Concrete commands
class LightCommand(ICommand):
    def __init__(self, light : Light):
        super().__init__()
        self.light = light
    
    def do(self):
        self.light.on()

    def undo(self):
        self.light.off()

class FanCommand(ICommand):
    def __init__(self, fan : Fan):
        super().__init__()
        self.fan = fan
    
    def do(self):
        self.fan.on()

    def undo(self):
        self.fan.off()

# Remote
class Remote:
    def __init__(self, num : int):
        self.num = num
        self.buttons = []
        self.pressed = []

        for _ in range(num):
            self.buttons.append(None)
            self.pressed.append(False)
    
    def setButtonCommand(self, command : ICommand, buttonNumber : int):
        if buttonNumber >= self.num or buttonNumber < 0:
            print(f"Invalid button number {buttonNumber}. Remote only have {self.num} buttons")
            return
        self.buttons[buttonNumber] = command
        self.pressed[buttonNumber] = False
    
    def pressButton(self, buttonNumber : int):
        if buttonNumber >= self.num or buttonNumber < 0:
            print(f"Invalid button number {buttonNumber}. Remote only have {self.num} buttons")
        elif self.buttons[buttonNumber]:
            if not self.pressed[buttonNumber]:
                self.buttons[buttonNumber].do()
                self.pressed[buttonNumber] = True
            else:
                self.buttons[buttonNumber].undo()
                self.pressed[buttonNumber] = False
        else:
            print(f"No command is given to button num {buttonNumber}")

if __name__ == "__main__":
    remote = Remote(2)
    light = Light()
    fan = Fan()
    remote.setButtonCommand(LightCommand(light), 0)
    remote.setButtonCommand(FanCommand(fan), 1)

    remote.pressButton(0)
    remote.pressButton(0)

    remote.pressButton(1)
    remote.pressButton(1)

    remote.pressButton(5)