#Converion of tuple
a = "Oneplus","Redmi","Sumsung","Nokia"
print("before conversion",type(a))
a = list(a)
print("after conversion",type(a))


a.append("Vivo")
print("\n",a)


a= tuple(a)
print("\n",type(a))
print(a)