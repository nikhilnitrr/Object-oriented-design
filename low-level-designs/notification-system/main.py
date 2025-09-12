from abc import ABC, abstractmethod

# Notification interface
class INotification(ABC):
    @abstractmethod
    def get_notification(self, str : str):
        pass

# Concrete notifications   
class TextNotification(INotification):
    def get_notification(self, str):
        return "<Text> " + str

class EmailNotification(INotification):
    def get_notification(self, str):
        return "<Email> " + str

# Decorators
class NotificationDecorator(INotification):
    def __init__(self, notification_obj : INotification):
        self.notification_obj = notification_obj

class SignatureDecorator(NotificationDecorator):
    def get_notification(self, str):
        return "<Signed> " + self.notification_obj.get_notification(str)

class CopyRightDecorator(NotificationDecorator):
    def get_notification(self, str):
        return "<All rights reserved> " + self.notification_obj.get_notification(str)

# Notification Strategy interface
class NotificationStrategy(ABC):
    @abstractmethod
    def notify(self):
        pass

class PushNotification(NotificationStrategy):
    def notify(self):
        print("Push notification sent")

class WhatsAppNotificatiom(NotificationStrategy):
    def notify(self):
        print("Whats app notification sent")

# Observers and observable
class NotificationObservable:
    def __init__(self):
        self.observers = []
        self.current_notification = None
    
    def get_data(self):
        return self.current_notification
    
    def notify(self):
        for observer in self.observers:
            observer.update()
    
    def set_data(self, data : str):
        self.current_notification = data
        self.notify()

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

class NotificationObserver(ABC):
    def __init__(self, observable : NotificationObservable):
        self.observable = observable
    
    @abstractmethod
    def update():
        pass

class Logger(NotificationObserver):
    def update(self):
        print("Logging" + self.observable.get_data())

class NotificationEngine(NotificationObserver):
    def __init__(self, observable):
        super().__init__(observable)
        self.notification_strategies = []
    
    def update(self):
        for strategy in self.notification_strategies:
            strategy.notify()
    
    def add_strategy(self, strategy : NotificationStrategy):
        self.notification_strategies.append(strategy)

# Notification Manager
class NotificationManager:
    _instance = None

    def __new__(cls, *args, **kwrags):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, observable : NotificationObservable):
        self.observable = observable
        self.notification_list = []
    
    def add_notification(self, notification : INotification, message : str):
        self.notification_list.append(notification)
        self.observable.set_data(notification.get_notification(message))



if __name__ == "__main__":

    message = "New item arrived"
    text_notification = TextNotification()
    email_notification = EmailNotification()

    # decorators
    text_notification = CopyRightDecorator(text_notification)
    email_notification = SignatureDecorator(email_notification)

    # notifiers
    notifier_one = PushNotification()
    notifier_two = WhatsAppNotificatiom()

    # concrete observable
    observable = NotificationObservable()

    # concrete observers
    observer_one = Logger(observable)
    observer_two = NotificationEngine(observable)

    # add strategies
    observer_two.add_strategy(notifier_one)
    observer_two.add_strategy(notifier_two)

    # add onservers
    observable.add_observer(observer_one)
    observable.add_observer(observer_two)

    manager = NotificationManager(observable)
    manager.add_notification(email_notification, message)