myList = []
myList = int(input().split())
myList.sort()
total = 0
average = 0

for i in myList:
    total += i
    average = total / len(myList)

print(f"{myList[-1]} {average}")