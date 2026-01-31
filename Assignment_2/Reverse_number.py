num  = int(input('Enter three digits'))

r1 = num % 10
num = num // 10
r2 = num % 10
num = num // 10
r3 = num % 10
num = num // 10

rev = 100 * r1 + 10 * r2 + r3
print(f'Reverse of Three Digits are {rev}')