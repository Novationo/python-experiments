number = int(input("Enter Number: "))
counter = 1

while counter < 13:
    product = number * counter
    print(f"{number} multiplied by {counter} equals {product}")
    counter = counter + 2

print("Loop has Finished!")