colors = []
colors = input("Enter a 5 PRIMARY colors separated by spaces: ").split()
# valid = ["red", "orange, yellow", "green", "blue", "purple", "indigo", "violet"]
check = set(colors)

if len(colors) != 5:
    print("Invalid input. Please enter exactly 5 colors.")
    exit()

if len(check) != 5:
    print("Invalid input. Please enter 5 unique colors.")
    print("Valid Colors: ", check)
    exit()

ascending = colors[:]
ascending.sort()

descending = colors[:]
descending.sort(reverse=True)


print("Alphabetical: ", ", ".join(ascending))
print("Reverse: ", ", ".join(descending))