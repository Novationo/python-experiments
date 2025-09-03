amount = 5

def printNames(nameList):
    if len(names) == amount:
        names.sort()
        print(". ".join(names), end=".")
    else:
        print("Wrong number of names")

names = input(f"Enter {amount} names with spaces between them: ").split()

print(names)

printNames(names)




