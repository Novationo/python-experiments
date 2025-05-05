myList = input().split()
total = 0
average = 0
maximum = float(myList[0])

for i in myList:
    if float(i) > maximum:
        maximum = float(i)

for i in myList:
    total += float(i)
    average = total / len(myList)

print(f"{maximum:.2f} {average:.2f}")

