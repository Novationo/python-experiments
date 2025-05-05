from math import prod


products = ("peanut butter", "jelly", "bread")
prices = (3.99, 2.99, 1.99)

choice = input("Select what you want to purchase: ").lower()
if choice in products:
    both = products.index(choice)
    print(products[both])
else:
    print("Item not found")