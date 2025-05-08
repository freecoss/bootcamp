my_dict = {}
while True:
    new_x = input("Enter new key(enter 'quit' to exit): ")
    if new_x.lower() == "quit":
        break
    new_y = input("Enter new value: ")
    my_dict[new_x] = new_y

print(my_dict)