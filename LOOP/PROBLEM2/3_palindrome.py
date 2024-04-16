# # WAP to find palindrome of integers

num = int(input("Enter a number here:\n"))
temp = num
rev = 0
while num>0:
    dig = num%10
    rev = rev*10+dig
    num =num // 10
if rev == temp:
    print("It is palindrome ")
else:
    print("It is not plaindrome number")
