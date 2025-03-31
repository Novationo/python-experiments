x = int(input())
y = int(input())

if y < x:
    print("Second integer can't be less than the first.")
else:
    for i in range(x, (y + 1), 5):
        print(i, end=" ")
    print()
