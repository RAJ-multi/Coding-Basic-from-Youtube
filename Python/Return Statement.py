def square (number):
    return number * number

number = int(input("Enter a number to square: "))
result = square(number)
print(result)

# alternative:

print(square(int(input("Enter a number to square: "))))

# what happens if we don't use return?
def square (number):
    print(number * number)

print(square(3)) # this will print 9, but the function itself returns None, so the output will be 9 followed by None