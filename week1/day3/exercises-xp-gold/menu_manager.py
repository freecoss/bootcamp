class MenuManager():
    def __init__(self,menu:list):
        self.menu = menu
        self.menu = [
            {
                "name": "Soup",
                "price": 10,
                "spice_level": "B",
                "gluten_index": False,
            },
            {
                "name": "Hamburger",
                "price": 15,
                "spice_level": "A",
                "gluten_index": True,
            },
            {
                "name": "Salad",
                "price": 18,
                "spice_level": "A",
                "gluten_index": False,
            },
            {
                "name": "French Fries",
                "price": 5,
                "spice_level": "C",
                "gluten_index": False,
            },
            {
                "name": "Beef bourguignon",
                "price": 25,
                "spice_level": "B",
                "gluten_index": True,
            }
        ]
    
    def add_item(self,name, price, spice, gluten):
        new_item = {
            "name": name,
            "price": price,
            "spice_level": spice,
            "gluten_index": gluten,
        }
        self.menu.append(new_item)
        print(f"{name} has been added to the menu.")
        
    def update_item(self,name, price, spice, gluten):
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice_level"] = spice
                item["gluten_index"] = gluten
                print(f"{name} has been updated.")
                return
        print(f"{name} not found in the menu.")
    
    def remove_item(self,name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} has been removed from the menu.")
                return
        print(f"{name} not found in the menu.")