total = float(input("Enter Bill Total: "))
tip = float(input("Enter Desired Tip Percent (< 1): "))

def check(total,tip):
    subtotal = total
    tipamount = total * tip
    total = total + (tipamount)
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tip: ${tipamount:.2f}")
    print(f"Total: ${total:.2f}")

if tip > 1:
    print("Enter tip as decimal less than 1")
    exit()
if tip <= 0.15:
    check(total,tip)
    print("You should leave more of a tip")
else:
    check(total,tip)

    '''doc strings can be easy to copy into documentation.'''