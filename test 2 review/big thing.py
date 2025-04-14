
# number = int(input("Enter a Number: "))
# symbol = str(input("Enter a Special Character: "))
number = 1 
symbol = " "

# 1.
# while number > 0 and len(symbol) == 1 :
#     number = int(input("Enter a Number: "))
#     symbol = str(input("Enter a Special Character: "))
#     print(number * symbol)

# 2a.
# while(True):
#     number = int(input("Enter a Number: "))
#     symbol = str(input("Enter a Special Character: "))
#     if number > 0 and len(symbol) == 1: # how to get out
#        print(number * symbol)
#     else:
#         print("Invalid Input")
#         exit() # instead of break

# 2c.
while(True):
    if number > 0 and len(symbol) == 1:
        number = int(input("Enter a Number: "))
        remainder = number % 2
        if remainder == 1:
            print(number * "^")
        elif remainder == 0:
            print(number * "*")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
        exit() # instead of break