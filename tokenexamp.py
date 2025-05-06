item_info = 'Bat 14 15'

item_tokens = item_info.split()
item = item_tokens[0]
quantity = item_tokens[1]
price = item_tokens[2]

print(f'{item} stock: {quantity}')
print(f'Price: {price}')