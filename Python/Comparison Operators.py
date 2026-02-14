while True:
    try:
        temparature = int(input("Enter the temparature: "))
        break
    except ValueError:
        print("Please enter numbers only")

if temparature > 30:
    print("It's a hot day")
elif temparature < 16:
    print("It's a cold day")
else:
    print("It's neither hot nor cold day")

print("Have a nice day!")


while True:
    try:
        name = input("Enter your name: ")
        if not name.isalpha():
            print("Please enter English characters only")
            continue
        break
    except ValueError:
        print("Please enter English characters only")
if len(name) < 3:
    print("Name must be at least 3 characters long")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters long")
else:
    print("Name looks good!")