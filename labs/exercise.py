# write a pay compute to give employess 1.5x money the hours worked above 40hr.

hours = int(input("Enter Hours:"))
rate = int(input("Enter Rate:"))
if hours > 0 and rate > 0:
    if hours > 40:
        overtime = hours - 40
        pay = (overtime * (rate * 1.5)) + (40 * rate)
    else:
        rate = rate
        pay = hours * rate
    print(f"Pay: ${pay:.2f}")
else:
    print("Error")