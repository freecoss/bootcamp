family = {}
while True:
    name = input("Enter family member name (enter 'done' to finish):")
    if name.upper() == "DONE":
        break
    age = input("Enter family member age: ")

    family[name] = age


family_total = 0
for x,y in family.items():
    if int(y)<3:
        family_total += 0
    elif int(y)>=3 and int(y)<=12:
        family_total += 10
    elif int(y)>12:
        family_total += 15
    
print(f"Total family is {family_total}")