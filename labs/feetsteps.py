def stepstoFt(steps):
    distFt = steps * 2.5
    return distFt
def feet_to_steps(feet):
    steps = feet/2.5
    return int(steps)

def main():
    dist = float(input())
    print(feet_to_steps(dist))


if __name__ == '__main__':
    # Type your code here.
    main()