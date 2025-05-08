class Zoo():
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []
    def add_animal(self, new_animal):
        for animal in self.animals:
            if animal == new_animal:
                print(f"{new_animal} already exists in the zoo.")
                break
        else:
            self.animals.append(new_animal)
    def get_animals(self):
        return self.animals
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been removed from the list successfully.")
        else:
            print(f"{animal_sold} already exists in the zoo.")

    def sort_animals(self):
        sorted_list = {}
        self.animals.sort()
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_list:
                sorted_list[first_letter] = []
        
            sorted_list[first_letter].append(animal)
    
        return sorted_list
    def get_groups(self):
        groups = self.sort_animals()
        for group,animal in groups.items():
            print(f"{group}: {animal}")

new_york_zoo = Zoo("New York Zoo")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Tiger")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Giraffe")
new_york_zoo.add_animal("Zebra")
new_york_zoo.add_animal("Monkey")
new_york_zoo.add_animal("Mouse")
new_york_zoo.add_animal("Kangaroo")
new_york_zoo.add_animal("Panda")
new_york_zoo.get_animals()
new_york_zoo.sell_animal("Tiger")
new_york_zoo.get_animals()
new_york_zoo.get_groups()
while True:
    animal = input("which animal should we add to the zoo(to exist enter 'done'): ")
    if animal == "done":
        break
    new_york_zoo.add_animal(animal)
        
new_york_zoo.get_groups()
