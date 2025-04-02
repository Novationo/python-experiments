num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 < num2:
    numTemp = num1
else:
    numTemp = num2
if num3 < numTemp:
    numTemp = num3
# else:
#     tiny = numTemp

print(numTemp)