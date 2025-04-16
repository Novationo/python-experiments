def print_popcorn_time(x):
    if x < 3:
        print("Too small")
    elif x > 10:
        print("Too large")
    else:
        seconds = 6 * int(x)
        print((f"{seconds} seconds"))


bag_ounces = int(input())
print_popcorn_time(bag_ounces)