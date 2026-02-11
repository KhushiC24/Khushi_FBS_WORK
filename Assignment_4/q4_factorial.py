num = int(input('Enter number for factorial: '))
factorial = 1
i = 1
while( i <= num ):
    factorial = factorial * i
    i += 1
print(f'Factorial of {num} is {factorial} ')