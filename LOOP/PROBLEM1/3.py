# Write a program to find sum of first 10 odd numbers using while loops
i=0
sum = 0

while i<=20:
    if i%2==1:
        sum+=i
    i+=1
print("Sum of odd numbers",sum)