change = int(input())
if change == 0:
    print("No change")
else:
    if change >= 100:
        dollars = change // 100
        if dollars == 1:
            print(f"{dollars} Dollar")
        else:
            print(f"{dollars} Dollars")
        change = change % 100

    # Calculate quarters
    if change >= 25:
        quarters = change // 25
        if quarters == 1:
            print(f"{quarters} Quarter")
        else:
            print(f"{quarters} Quarters")
        change = change % 25

    # Calculate dimes
    if change >= 10:
        dimes = change // 10
        if dimes == 1:
            print(f"{dimes} Dime")
        else:
            print(f"{dimes} Dimes")
        change = change % 10

    # Calculate nickels
    if change >= 5:
        nickels = change // 5
        if nickels == 1:
            print(f"{nickels} Nickel")
        else:
            print(f"{nickels} Nickels")
        change = change % 5

    # Calculate pennies
    if change > 0:
        if change == 1:
            print(f"{change} Penny")
        else:
            print(f"{change} Pennies")
