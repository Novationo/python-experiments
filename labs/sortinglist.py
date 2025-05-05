myList = input().split()
negList = []

for i in myList:
    if int(i) < 0:
        negList.append(i)

negList = sorted(negList, key=int, reverse=True)
print(" ".join(negList), end=" ")