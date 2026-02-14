while True:
    try:
        weight = float(input("Enter your weight: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number only.")

unit = input("Is this weight in (K)g or (L)bs? ").upper()
if unit == 'K':
    converted_weight = weight * 2.20462
    print(f"Your weight in pounds is: {converted_weight:.2f} lbs")
elif unit == 'L':
    converted_weight = weight / 2.20462
    print(f"Your weight in kilograms is: {converted_weight:.2f} kg")
else:
    print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")