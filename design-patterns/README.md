# Most commonly used design patterns have been implemented in python programming language
(For detailed explanation of each design pattern , refer : https://nikhilchandrakar.hashnode.dev/)
## Singleton design pattern :
    - Singleton design pattern is one of the most commonly used design patterns. We use singleton design pattern when we need only one instance of a class.
    - For example : Logger, Configuration manager, Parking station, Chess-Board
## Thread safe singleton design pattern :
    - Singleton design pattern that ensures that even if multiple threads are running, only one instance is created.
## Strategy design pattern :
    - Strategy design pattern can be defined as a design pattern that defines a family of algorithms and put them into separate classes so that they can be changed at run-time.
## Decorator design pattern :
    - Decorator pattern attaches additional responsibilities to an object dynamically. Decorator provides a flexible alternative to subclassing for extending functionality.
## Factory design pattern :
    - Factory design pattern is used to separate an application's business logic from its object creation logic.
    - The client delegates object creation to a factory, allowing the client to focus solely on business logic.
    - There are three main types of factory design patterns:
        + Simple Factory: A concrete factory class that creates only one type of object.
        + Factory Method: An abstract factory class that delegates object creation to concrete subclasses, each creating one type of object.
        + Abstract Factory: Similar to the factory method, but capable of creating families of related objects.
## Command design pattern :
    - In command design pattern, the request or command sent by client is encapsulated as an object so that the command is undoable when needed. And command can be changed at runtime.
## Observer design pattern :
    - Observer design pattern is used when you want to alert or notify the observer if anything changes in the observable.
## Adapter design pattern :
    - The adapter design pattern allows objects with incompatible interfaces to work together by introducing an adapter that acts as a bridge between them
    - For example : Your latest code cannot use legacy code directly, hence you need an adapter so that your latest code can execute legacy code.