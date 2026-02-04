import random

user_id = 'khushi'
password = '2426'

id = input('Enter userid: ')
p = input('Enter password: ')
if user_id == id and password == p:
    print('Login Successful')
else:
    print('Login Unsccessful')
captcha = random.randint(1000, 9999)
print(captcha)
c =int(input("Enter the captcha: "))
print(c)
if c == captcha:
    print("Success")
else:
    print("Failed")