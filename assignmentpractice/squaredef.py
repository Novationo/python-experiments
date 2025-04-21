def long(x):
    print("*" * x)
def height(x,y):
    for i in range(y-2):
        print(f"*{" " * (x-2)}*")

length = int(input("enter length of box: "))
tall = int(input("enter height of box: "))

def main():
    long(length)
    height(length,tall)
    long(length)

if __name__ == "__main__":
    main()

# dont use global variables
b = 10 # this bad, make specific!