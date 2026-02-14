number = 9
i = 0
while i < 3:
    try:
        guess = int(input("Guess the number: "))
    except ValueError:
        print("Please enter only a number!")
        continue
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Congratulations! You've guessed the number.")
        break
    i += 1
else:
    print("You failed!")