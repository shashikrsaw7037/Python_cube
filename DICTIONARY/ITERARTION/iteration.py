Student = {"name":"John","class":"6th","roll-no":23}
#printing all the key names one by one
for x in Student:
    print(x)
print("*"*30)

#printing all the values names one by one
for x in Student:
    print(Student[x])
print("*"*30)

#using value dunction
for x in Student.values():
    print(x)
print("*"*30)

# using items functions  // for both keys and values
for x,y in Student.items():
    print(x,"-",y)