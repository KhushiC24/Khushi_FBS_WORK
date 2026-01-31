cost_price = float(input('Enter Cost Price'))
discount = int(input('Enter Discount '))

Selling_price = cost_price * (1-(discount/100))

print(f'Selling Price of the book is {Selling_price}')