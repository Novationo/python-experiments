types = ["*", "/", "+", "-"]

def calculate(num1, num2, type):
    if type == "*":
        return num1 * num2
    elif type == "/":
        return num1 / num2
    elif type == "+":
        return num1 + num2
    elif type == "-":
        return num1 - num2
    

print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())
print("Enter the type: ")
type = input()

if type not in types:
    print("Invalid type")
else:
    print(calculate(num1, num2, type))