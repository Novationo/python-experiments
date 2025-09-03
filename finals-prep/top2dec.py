numbers = input("Enter each number followed by a space: ").split()


if len(numbers) == 5:
    min1 = min(numbers)
    max1 = max(numbers)
    print(numbers)
    print("Min/Max:", min1, max1)


    secondmin = numbers[:]
    numbers.pop(0)
    numbers.pop(-1)

    print(numbers)
    min2 = min(numbers)
    max2 = max(numbers)
    print("Min/Max:", min2, max2)

