def greet(first_name, last_name):                            # function definition must be before the function call
    print (f"hi, {first_name} {last_name}!")
    print ("welcome to python")

print("starting")
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
greet(first_name, last_name)       
print("and")      
greet(first_name="John", last_name="Doe")                      # function call and here first_name and last_name are keyword arguments. We can change the order of the arguments when we use keyword arguments.
print("ending")