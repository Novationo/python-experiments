
def output_vals(x,y):
    for i in range(x,y+1):
        mult = i * 10
        print(mult, end=" ")



numberA = int(input())
numberB = int(input())

print('Testing static input: ')
output_vals(2, 4)
print(f'\nTesting user input: ')
output_vals(numberA, numberB)