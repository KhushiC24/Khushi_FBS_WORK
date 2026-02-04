num = int(input("Enter Number: "))
temp = num

r1 = num % 10
num = num // 10
r2 = num % 10
num = num // 10
r3 = num % 10
num = num // 10

rev = r1 * 100 + r2 *10 + r1

if rev == temp:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not Palindrome")