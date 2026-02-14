for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")

numbers = [5,2,5,2,2]
for number in numbers:
    output = ''
    for count in range(number):
        output += 'X'
    print(output)

# alternative way using string multiplication
for number in numbers:
    print('X' * number)