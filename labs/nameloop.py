names = []
adding = True
while adding:
    name = input("Enter name, press 'q' to quit: ")
    if name == "q":
        adding = False
        break
    else:
        names.append(name)
        names.sort()
        print("Names:",", ".join(names))
