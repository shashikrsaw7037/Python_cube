#WAP to create a billing system

while True:
    name = (input("Enter customers name:"))
    total =0

    while True:
        print("Enter the amount and quantity")
        amount=float(input("Enter amount :"))
        quantity=float(input("Enter quantity :"))

        total = amount * quantity

        repeat = input("Do you want to add more items ?(Yes/No)")

        if(repeat =="No"or repeat == "no"):
            break
        print("-",*40)
        print("Nmae:",name)
        print("AMount to paid:",total)
        print("-"*40)

        print("***********HAPPY SHOOPING*****************")

        repeat1= input("Do you want to go to next customer ?(Yes/No)")
        if repeat1 == "no" or repeat1=="No":
            break