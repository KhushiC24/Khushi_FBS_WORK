def reverse(num, rev=0):
    if num == 0:
        return rev
    return(reverse(num//10, rev*10 + num%10))
def isPalindrome(num):
    return num == reverse(num)

num = int(input("Enter Number: "))
res = isPalindrome(num)
print(res)