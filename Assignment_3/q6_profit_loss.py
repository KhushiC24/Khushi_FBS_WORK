cost_price = float(input('Enter Cost Price: '))
selling_price = float(input('Enter selling price: '))

profit = selling_price - cost_price
loss = cost_price -selling_price

if selling_price > cost_price:
    print(f'Profit {profit}.')
elif cost_price > selling_price:
    print(f'Loss {loss}.')
else:
    print('No Profit No Loss')