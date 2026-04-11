def strong(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10 
        fact = 1
        for i in range(1, digit + 1):
            fact  = fact * i
        sum += fact
        temp //= 10
    return sum == num 


num = int(input("Enter Number To check: "))
res = strong(num)
print(res)



