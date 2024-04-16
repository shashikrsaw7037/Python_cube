## WAP to check if a number is prime or not
2,3,5,7,11
num  = int(input("Enter number"))

if num <=1:
    print("It is not a prime number")
else:
    for i in range(2,num):
        if num %i==0:
            print("It is not a prime number")
            break
    else:
        print(" It is prime number")
        
print(7%2)