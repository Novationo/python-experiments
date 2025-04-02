# first eq
a = int(input())
b = int(input())
c = int(input())

# sencond eq
d = int(input())
e = int(input())
f = int(input())

solution = False

for x in range(-10, 11):
    for y in range(-10, 11):
        if (a*x) + (b*y) == c and (d*x) + (e*y) == f:
            print(f"x = {x} , y = {y}")
            solution = True
            break
        if solution:
            break
if not solution:
    print("There is no solution")