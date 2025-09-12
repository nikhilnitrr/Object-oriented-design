from menu import MenuItem
from uuid import uuid4

class Restaurant:
    def __init__(self, name, address):
        self.id = uuid4()
        self.name = name
        self.address = address
        self.menuItems = []
    
    def addMenuItem(self, menuItem : MenuItem):
        self.menuItems.append(menuItem)
