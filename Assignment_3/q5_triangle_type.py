a = int(input('Enter 1st side: '))
b = int(input('Enter 2nd side: '))
c = int(input('Enter 3rd side: '))

if a == b == c:
    print('Triangle is Equilateral')
elif a == b or b == c or a == c:
    print('TTriangle is Isosceles')
else:
    print('Triangle is Scalene')