car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"

car_list = [car.strip() for car in car_string.split(",")]

print(f"There are {len(car_list)} manufacturers in the list.")

print("Manufacturers in reverse alphabetical order (Z-A):")
print(sorted(car_list, reverse=True))

count_with_o = sum(1 for car in car_list if 'o' in car.lower())
print(f"{count_with_o} manufacturer(s) have the letter 'o' in their name.")

count_without_i = sum(1 for car in car_list if 'i' not in car.lower())
print(f"{count_without_i} manufacturer(s) do not have the letter 'i' in their name.")

car_list_with_duplicates = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
unique_car_list = list(set(car_list_with_duplicates))
print(f"After removing duplicates, there are {len(unique_car_list)} unique manufacturers.")
print("Unique manufacturers (comma-separated):")
print(", ".join(unique_car_list))

print("Manufacturers A-Z, but with letters in each name reversed:")
for name in sorted(unique_car_list):
    print(name[::-1])
