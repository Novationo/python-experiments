names = []
adding = True
while adding:
    name = input()
    if name == "q":
        adding = False
        break
    else:
        names.append(name)
        names.sort()
        print(", ".join(names))
