for item in "Phython":
    print(item)
for name in ["mosh", "john", "sarah"]:
    print(name)
for number in range(10):
    print(number)
for number in range(5, 10):
    print(number)
for number in range(5, 10, 2):
    print(number)

prices = []
while True:
    try:
        n = int(input("How many prices? "))
        break
    except ValueError:
        print("Enter number only")

for i in range(n):
    while True:
        try:
            p = int(input("Enter price: "))
            prices.append(p)
            break
        except ValueError:
            print("Enter number only")

total = 0
for price in prices:
    total += price
print(f"Total: {total}")