class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
    
    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'congrats to the {self.last_name} family for the new born {kwargs["name"]}')
        
    def is_18(self,name):
        for member in self.members:
            if member["name"] == name:
                return member["age"]>=18
        return False
    
    def family_presentation(self):
        print(f'the family {self.last_name} has the following members :')
        for member in self.members:
            print(f" - {member['name']}, {member['age']} years old, {member['gender']}")


family_members =[
        {'name':'Michael','age':35,'gender':'Male','is_child':False},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
    ]
test = Family(family_members, "test")
test.born(name='Emily', age=0, gender='Female', is_child=True)
if(test.is_18("Michael")):
    print('Michaek is more than 18yo')
else:
    print('Michaek is less than 18yo')
test.family_presentation()
