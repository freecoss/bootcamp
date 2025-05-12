class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_bengal = Bengal('test1',2)
my_chartreux = Chartreux('test2',3)
my_siamese = Siamese('test3',1)

all_cats = [my_bengal, my_chartreux, my_siamese]
sara_pets = Pets(all_cats)

sara_pets.walk()