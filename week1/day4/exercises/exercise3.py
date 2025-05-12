import random
from exercise2 import Dog
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
        dog_names = [self.name] + [dog.name for dog in args]
        print(f"{', '.join(dog_names)} all play together")
    
    def do_a_trick(self):
        tricks = [
            f"{self.name} does a barrel roll",
            f"{self.name} stands on his back legs",
            f"{self.name} shakes your hand",
            f"{self.name} plays dead"
        ]
        if(self.trained == True):
            print(random.choice(tricks))
            
