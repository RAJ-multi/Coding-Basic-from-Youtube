weather = input("Is it a hot day? (yes/no): ").lower()
if weather == "yes":
    print("It's a hot day.")
    print("Drink plenty of water.")
    print("Enjoy your day!")
elif weather == "no":
    is_cold = input("Is it a cold day? (yes/no): ").lower()
    if is_cold == "yes":
        print("It's a cold day.")
        print("Wear warm clothes.")
        print("Enjoy your day!")
    elif is_cold == "no":
        print("It's a lovely day.")
        print('Dress lightly.')
        print("Enjoy your day!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")