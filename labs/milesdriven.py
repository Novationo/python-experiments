# Define your function here.
def driving_cost(mpg,dpg,miles):
    perMile = dpg/mpg
    costMile = perMile * miles
    return costMile


def main():
    milesPG = float(input())
    dollarPG = float(input())
    mDriven = [10, 50, 400]
    print(driving_cost(milesPG,dollarPG,mDriven))


if __name__ == '__main__':
    # Type your code here.
    main()

