customers = {"name": "Alice", "age": 30, "city": "New York", "is_verified": True}
print(customers.get("name"))
print(customers.get("Age, 25"))  # Default value if key not found
customers["age"] = 31  # Update age
customers["email"] = "Alice126@gmail.com"  # Add new key-value pair
print(customers.get("email"))

number = {1: "one", 2: "two", 3: "three", 123: "one two three"}
input_number = int(input("Enter a number (1-3): "))
print(number.get(input_number, "Number not found"))  # Default message if key not found

#alternative way to create a dictionary

phone_number = input("Enter your phone number: ")
digit_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for digit in str(phone_number):
    output += digit_mapping.get(digit, "!") + " "
print(output)