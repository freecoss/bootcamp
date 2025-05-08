class Cat():
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

first_cat = Cat("elena",20)
second_cat = Cat("martha",12)
third_cat = Cat("yara",10)
def oldest_cat(cat1:Cat, cat2:Cat, cat3:Cat):
    if cat1.age > cat2.age :
        if  cat1.age > cat3.age:
            return cat1
        else:
            return cat3
    elif cat2.age > cat3.age:
        return cat2
    else:
        return cat3

print("The oldest cat is : "+ oldest_cat(first_cat, second_cat, third_cat).name +", and is " + str(oldest_cat(first_cat, second_cat, third_cat).age) + " years old.")