def greet(name):                            # function definition must be before the function call
    print (f"hi, {name}!")
    print ("welcome to python")

print("starting")
name = input("Enter your name: ").title()
greet(name)                                   # function call
print("ending")