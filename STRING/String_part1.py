#len(),count(),upper(),lower()
# index(),capitalize(),casefold(), find(),format(),center

a="Harry Potter and The Goblet of Fire"

print(a)#Harry Potter and The Goblet of Fire
print(len(a))#35
print("Count",a.count("H")) # O/P is 1 ,  Beasce of python is case sensitive. Becasuse of that capital H ,it will count separate and h it will count separate
print("INDEX",a.index("o")) # O/P is  7, In that there are two [o] ,It will display 1st o
print(a.index("o",15,35))   # O/p is 22 ,It will show o in between of index 15 index 35
print(a.capitalize())       # O/p is Harry potter and the goblet of fire
print(a.casefold())         # O/P is harry potter and the goblet of fire
print(a.lower())            # O/P is harry potter and the goblet of fire
print(a.upper())            # O/P is HARRY POTTER AND THE GOBLET OF FIRE
print(a.find("o",15,34))    # O/P is 22


name = "John"
print("My name is ", format(name)) #O/P My name is  John


name1 = "Shashi"
b="My name is {}"
print(b.format(name1))  #O/P My name is Shashi

print(name1.center(20,"*"))# *******Shashi*******
print(len(name1.center(20,"*"))) # O/P is 20