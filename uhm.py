stop = -10
total = 0
for number in [4, 4, 4, 6, 3, 5]:
    print(number, end=' ')
    total -= number
    if total < stop:
        print('*')
        break
else:
    print(f'| {total}')
print('done')