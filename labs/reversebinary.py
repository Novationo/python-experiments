
x = int(input())
output = []

while x > 0:
    y = x % 2
    output.append(str(y))
    x = x // 2

print("".join(output))