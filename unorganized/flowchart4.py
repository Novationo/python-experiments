a = 1 
total = 0
dayIncome = 0
while a > 0: 
    intereiorQ = input("Enter interior Quality\n")
    lotSize = input("Enter Lot Size in Square Feet\n")
    houseSize = input("Enter House Size in Square Feet\n")
    
    if int(intereiorQ) == 1:
        lotSize = lotSize / 500
        total += 1000 * lotSize
        houseSize = houseSize / 100
        total += houseSize * 500
    elif int(intereiorQ) == 2:
        lotSize = lotSize / 500
        total += 700 * lotSize
        houseSize = houseSize / 100
        total += houseSize * 400
    elif int(intereiorQ) == 3:
        lotSize = lotSize / 500
        total += 700 * lotSize
        houseSize = houseSize / 100
        total += houseSize * 400
    else:
        print("House Cost is $",total)

