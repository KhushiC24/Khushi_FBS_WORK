num  = int(input('Enter three digits'))

r1 = num % 10
num = num // 10
r2 = num % 10
num = num // 10
r3 = num % 10
num = num // 10

sum = r1  + r2 + r3

print(f'Sum of Three Digits are {sum}')