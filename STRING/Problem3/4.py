## Write a program to find number of vowels in string

a = (input("enter anything here: "))
vowels = 0
for i in a:
    if i=="a" or i=="e" or i =="i" or i =="u" or i =="A" or i =="E" or i =="O" or i=="I" or i =="U":
        vowels+=1
print("The number of vowels ",vowels)
