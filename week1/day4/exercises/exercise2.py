class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def bark(self):
        return f'{self.name} is barking'
    
    def run_speed(self):
        return (int(self.weight)/int(self.age))*10
    
    def fight(self, other_dog:object):
        won_dog = 'draw'
        if(self.run_speed()*int(self.weight)>other_dog.run_speed()*int(other_dog.weight)):
            won_dog = f'{self.name} won the fight'
        elif(self.run_speed()*int(self.weight)<other_dog.run_speed()*int(other_dog.weight)):
            won_dog = f'{other_dog.name} won the fight'
        return won_dog

first = Dog('tiger', 3 , 50)
second = Dog('hitl', 2 , 40)
third = Dog('ayou', 5 , 60)
print(first.fight(second))