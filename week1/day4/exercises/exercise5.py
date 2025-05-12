from exercise4 import Family
class TheIncredibles(Family):
    def __init__(self, members, last_name):
        super().__init__(members, last_name)
    
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    print(f"{name}'s power: {member['power']}")
                else:
                    raise Exception(f"{name} is not over 18 years old!")
        return False

    def incredible_presentation(self):
        print("*Here is our powerful family**")
        super().family_presentation()
        print("\nIncredible Names and Powers:")
        for member in self.members:
            print(f" - {member['name']} ({member['incredible_name']}): {member['power']}")
            
incredible_members = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
]

incredibles_family = TheIncredibles(incredible_members, "Incredibles")

incredibles_family.incredible_presentation()
incredibles_family.born(name = "Jack", age =0, gender = "Male", is_child = True, power= "Unknown Power", incredible_name='unknown')
incredibles_family.incredible_presentation()