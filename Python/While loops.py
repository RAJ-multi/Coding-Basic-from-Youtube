while True:
    try:
        i = int(input("enter i value for loops under 16 : "))
        break
    except ValueError:
        print("Invalid input! Please enter a number only.")

if i > 16:
    print("The entered number is bigger than 16, loop not executed.")
else:
    while i <= 16:
        print('*' * i)
        i = i + 1
    print("loop ended")