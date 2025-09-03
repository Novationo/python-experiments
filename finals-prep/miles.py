previous = int(input("Enter the previous miles: "))
current = int(input("Enter the current miles: "))

if previous > current:
    print("Invalid input")

if (current - previous) > 3000:
    print("Oil change needed")
else:
    print("No oil change needed")





