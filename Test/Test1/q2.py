p = int(input('Enetr principal'))
r = float(input('Enter Rate '))
t = int(input('Enter Time '))

r = r / 100
si = (p * r ) * t/100

print(f'Simple Interest{si}')