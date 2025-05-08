import random
class MyList():
    def __init__(self, letters:list):
        self.letters = letters
        
    def reverse_list(self):
        return self.letters.reverse()
    
    def sort_list(self):
        return self.letters.sort()
    
    def generate_list(self):
        new_list = []
        for i in range (1, len(self.letters)+1):
            new_list.append(random.randint(1, 100))
        return new_list
