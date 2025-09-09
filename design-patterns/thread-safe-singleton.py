import threading

class Singleton(threading.Thread):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        super().__init__()
        print(self)


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    print(s1==s2)