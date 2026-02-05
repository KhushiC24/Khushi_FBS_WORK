area = int(input('Enter Area'))
cost_i = int(input('Enter Cost of Interior wall'))
cost_e = int(input('Enter Cost of Exterior wall'))

cost_in = area * 8 * cost_i
cost_ex = area * 7 * cost_e

print(f'Cost of Interior Wall is {cost_in}')
print(f'Cost of Interior Wall is {cost_ex}')