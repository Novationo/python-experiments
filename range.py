myList = input().split()
range = input().split()

rangeList = []

lower = range[0]
upper = range[1]

for i in myList:
    if int(i) >= int(lower) and int(i) <= int(upper):
        rangeList.append(i)

print(",".join(rangeList), end=",")