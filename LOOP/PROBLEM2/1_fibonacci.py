# #WAP to get Fibonacci series upto 10 numbers 
# a=0
# b=1
# for i in range(2,11):
#     c=a+b
#     print(c,end=" ",)
#     a=b
#     b=c
# print("\nfibonacci\n",c)




# a =0
# b =1
# n = int(input("Enter number here:"))
# if n==1:
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c=a+b
#         a=b
#         b=c
#         print(c)



x = 0
y = 1
i=1
n=11
while i<n:
    print(x)
    z=x+y
    x=y
    y=z
    i+=1
