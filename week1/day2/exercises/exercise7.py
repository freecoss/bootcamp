import random
def get_random_temp(season):
    # first version
    # return random.randint(-10, 40)

    # new version
    if season == "winter":
        # I changed from randint to random so that the temperature can be a floating-point number
        return round(random.uniform(-10, 16),2)
    elif season == "spring":
        return round(random.uniform(0, 24),2)
    elif season == "summer":
        return round(random.uniform(24, 40),2)
    elif season == "autumn":
        return round(random.uniform(0, 32),2)
    else:
        print("Invalid season. Please enter 'winter', 'spring', 'summer', or 'autumn'.")
        return None
    


# Test the function
# print(get_random_temp())

def main():
    season = ""
    month = int(input("Enter the month: ").lower())
    if month in [12, 1, 2]:
        season = "winter"
    elif month in [3, 4, 5]:
        season = "spring"
    elif month in [6, 7, 8]:
        season = "summer"
    elif month in [9, 10, 11]:
        season = "autumn"
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
        return
    temp = get_random_temp(season)
    print(f"the temperature right now is {temp} degrees Celsius")
    if temp<0:
        print("Brrr, that's freezing! Wear some extra layers today")
    elif temp>=0 and temp<16:
        print("Quite chilly! Don't forget your coat")
    elif temp>=16 and temp<=23:
        print("A bit chilly, but not too bad")
    elif temp>=24 and temp<32:
        print("Perfect weather! Enjoy your day")
    elif temp>=32 and temp<=40:
        print("It's getting hot! Stay hydrated and cool")

main()