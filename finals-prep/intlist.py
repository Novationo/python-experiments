list = input("Enter a list of integers: ").split()

min = min(list)
max = max(list)

print("Given Integers:",", ".join(list), end=".\n")
print("Min/Max:", min,"/", max)

total = 0

noend = list[:]

for (i) in noend:
    noend.pop(-1)
    total += int(i)

print("Sum:", total)





