# Complex sub-system
class CPU:
    def start(self):
        print("Starting the CPU")

class Memory:
    def initialize(self):
        print("Initializing the memory")

class Power:
    def on(self):
        print("Turning ON power")

class Fan:
    def start(self):
        print("Start the fan")

class BIOS:
    def boot(self, cpu : CPU , memory : Memory):
        print("Booting your computer system")
        cpu.start()
        memory.initialize()

# Facade : Responsible for managing the complex sub-system
class Facade:
    def __init__(self, cpu : CPU , memory : Memory, power : Power, fan : Fan, bios : BIOS):
        self.cpu = cpu
        self.memory = memory
        self.power = power
        self.fan =  fan
        self.bios = bios

    def start_computer(self):
        self.power.on()
        self.fan.start()
        self.bios.boot(self.cpu, self.memory)

# Client : Doesn't know anything about the complex subsystem
class Client:
    def __init__(self, facade : Facade):
        self.facade = facade
    
    def start_computer(self):
        self.facade.start_computer()

if __name__ == "__main__":
    f = Facade(CPU(), Memory(), Power(), Fan(), BIOS())
    c = Client(f)
    c.start_computer()