n = int(input('Enter Number to chcek perfect number: '))
sum = 0
for i in range(1,n):
    if(n % i == 0):
        sum += i
if n == sum:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')