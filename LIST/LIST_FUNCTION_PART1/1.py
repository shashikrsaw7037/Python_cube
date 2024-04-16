a=["Thor","Hulk","Captain America", "Hulk"]
print("1   :",a)

#to find the length of list
print("2   :",len(a))

# to count an occurence of a particular element
print("3   :",a.count("Hulk"))

# to add to the lsit
a.append("Spiderman")
print("4   :",a) #append value at the last

# to add to a specific loaction
a.insert(1,"Vision")
print("5   :",a)

#to remove from a list
a.remove("Spiderman")
print("6   :",a)

# to remove from a certain loaction
print("7   :",a.pop(1))
print("8   :",a)
