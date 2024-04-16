# endswith() -Returns true if the string ends with the specified value
a = "Harry Potter"
print(a.endswith("r")) #O/P is True
print(a.endswith("t",6,9))#O/P is True

# startwith() -Returns true if the string starts with the specified value
B = "Harry Potter"
print(B.startswith("H"))#O/P is True
print(B.startswith("P",6,9))#O/P is True

#swapcase() - Swaps cases lowercase becomes uppercase and vice-versa
A="Harry Potter"
print(A.swapcase())#O/P is hARRY pOTTER

#strip()- Returns a trimmed version of the string
T = "***********                      HARRY Potter   .................."
print(T) #O/P --> ***********                      HARRY Potter   ..................
print(T.strip("*, ,."))#o/p is HARRY Potter

# rjust() - Returns a right justified version of the string
L= "Shashi"
x=L.rjust(20,"~")
print(x,"is good")#O/P is [~~~~~~~~~~~~~~Shashi]20 is good
print(len(x))     # 20 when rjust shift right it will take all 20 character from x


# replace()- Return a sting where a specified value is replaced with a specified value 
a = "my name is john"
print(a)#my name is john
print(a.replace("john","Lisa")) # O/P is my name is Lisa# If instead of john differnt name we put it will show prevoius output
#my name is Lisa
