a = int(input('Enter 1st Side: '))
b = int(input('Enter 2nd Side: '))
c = int(input('Enter 3rd Side: '))

if(a + b >c) and (a + c >b) and (b + c >a):
    print('Triangle is Valid')
else:
    print('Triangle is not Valid')