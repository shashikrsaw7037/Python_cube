a = "Oneplus","Vivo","Redmi","Sumsung","Nokia"
print(a[1:3])   
print(a[:3])
print(a[2:])
print(a[1::2])
print(a[2::-1])

# ('Vivo', 'Redmi')
# ('Oneplus', 'Vivo', 'Redmi')
# ('Redmi', 'Sumsung', 'Nokia')
# ('Vivo', 'Sumsung')
# ('Redmi', 'Vivo', 'Oneplus')


# with for loop
for i in a:
    # print(a[i])   //error
    print(i)

# along with range and length in for loop
for i in range(len(a)):
    print(a[i])
    print(a)
    print(i)