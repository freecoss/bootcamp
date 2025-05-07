import random

def random_number():
    value = int(input("Enter a number between 0 and 100: "))
    if value<0 and value>100:
        return "Please enter a number between 0 and 100"
    else:
        random_number = random.randint(0,100)
        if value == random_number:
            print("You guessed it!")
        elif value != random_number:
            print(f"you guessed wrong! your number is {value} and the random number is {random_number}")

random_number()