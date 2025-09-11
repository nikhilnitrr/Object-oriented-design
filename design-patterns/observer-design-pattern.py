from abc import ABC, abstractmethod

# Interface for observer
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass

# Abstract base class for observable
class Observable(ABC):
    def __init__(self):
        super().__init__()
        self.observers = []
    
    def add_observer(self, observer : Observer):
        self.observers.append(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update()
    
    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self):
        pass

# Concrete classes
class TemperatureObservable(Observable):
    def __init__(self):
        super().__init__()
        self.current_temperature = 25
    
    def get_value(self):
        return self.current_temperature
    
    def set_value(self, updated_temperature):
        self.current_temperature = updated_temperature
        self.notify()

class TemperatureObserver(Observer):
    def __init__(self, observable : Observable):
        super().__init__()
        self.observable = observable
    
    def update(self):
        print(self.observable.get_value())

if __name__ == "__main__":
    temp_observable = TemperatureObservable()
    temp_observer_1 = TemperatureObserver(temp_observable)
    temp_observer_2 = TemperatureObserver(temp_observable)

    temp_observable.add_observer(temp_observer_1)
    temp_observable.add_observer(temp_observer_2)

    temp_observable.set_value(40)
