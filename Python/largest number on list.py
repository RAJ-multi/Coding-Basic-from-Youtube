try:
    count_input = input("Enter the number of elements in the list: ").strip()
    if count_input == "":
        print("The list is empty.")
        exit()
    count = int(count_input)
except ValueError:
    print("Only numbers allowed.")
    exit()

numbers = []
for i in range(count):
    num_input = input(f"Enter element {i+1}: ").strip()
    if num_input == "":
        print("The list is empty.")
        exit()
    try:
        num = int(num_input)
        numbers.append(num)
    except ValueError:
        print("Only numbers allowed.")
        exit()

if not numbers:
    print("The list is empty.")
elif len(numbers) == 1:
    print("One number can't be a list, enter more than one number.")
else:
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    print("The largest number in the list is:", max_num)