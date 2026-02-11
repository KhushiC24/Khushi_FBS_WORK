n = int(input('Enter value upto you want sum of series: '))
i = 1
sum = 0
while(i <= n):
    sum = sum + i
    print(i)
    i += 1
print(f'Sum of Series upto {n} is {sum} ')