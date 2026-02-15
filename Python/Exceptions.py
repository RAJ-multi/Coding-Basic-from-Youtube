while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break
    except ValueError:
        print("Please enter a valid number for age. Try again.")

while True:
    try:
        income = float(input("Enter your income: "))
        print("Your income is:", income)
        break
    except ValueError:
        print("Please enter a valid number for income. Try again.")

while True:
    income_type = input("Enter your income type (per month or per year): ").strip().lower()
    if income_type == "per month":
        print("Your per hour income is:", income / 240)
        break
    elif income_type == "per year":
        print("Your per hour income is:", income / 240 / 12)
        break
    else:
        print("Invalid input for income type. Try again.")