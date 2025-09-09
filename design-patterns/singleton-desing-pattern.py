class Singleton:
    
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # self is now pointing to the instance of the singleton class
        print(self)

if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()