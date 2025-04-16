name = input()

while name.lower() != "yes":
    try:
        name = int(name)
        print(name)
    except:
        print("You didn't end a number")


