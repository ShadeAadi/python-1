print("SUMthing.")
print("")
print("What simple opperation would you like to preform on two integers?")
print("(addition/subtraction/multiplication/division)")
print("")
op = input("")
print("")
if op == "addition":
    print("Enter the first number:")
    print("")
    a = input("")
    if a == "chicken sandwich":
        print("")
        print("Nanditha, no.")
    else:
        x = int(a)
        print("")
        print("Enter the second number:")
        print("")
        y = int(input(""))
        z = x+y
        print("")
        print("The sum of",x,"and",y,"is:")
        print("")
        print(z)
elif op == "subtraction":
    print("Enter the first number:")
    print("")
    a = input("")
    if a == "chicken sandwich":
        print("Nanditha, no.")
    else:
        x = int(a)
        print("")
        print("Enter the second number:")
        print("")
        y = int(input(""))
        z = x-y
        print("")
        print("The difference of",x,"and",y,"is:")
        print("")
        print(z)
elif op == "multiplication":
    print("Enter the first number:")
    print("")
    a = input("")
    if a == "chicken sandwich":
        print("Nanditha, no.")
    else:
        x = int(a)
        print("")
        print("Enter the second number:")
        print("")
        y = int(input(""))
        z = x*y
        print("")
        print("The product of",x,"times",y,"is:")
        print("")
        print(z)
elif op == "division":
    print("Enter the first number:")
    print("")
    a = input("")
    if a == "chicken sandwich":
        print("Nanditha, no.")
    else:
        x = int(a)
        print("")
        print("Enter the second number:")
        print("")
        y = int(input(""))
        z = x/y
        print("")
        print("The quotient of",x,"by",y,"is:")
        print("")
        print(z)
else :
    print("Input invalid.")
input("")

