def driving_cost(mpg, dpg, mDrive):
    gallons = mDrive / mpg
    cost = gallons * dpg
    return cost

def main():
    mpg = float(input())
    dpg = float(input())

    distances = [10, 50, 400]
    for distance in distances:
        cost = driving_cost(mpg, dpg, distance)
        print(f'{cost:.2f}')

if __name__ == '__main__':
    main()
