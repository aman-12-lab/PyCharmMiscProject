#Make simple Supermarket -program,

prices = [10,14,22,33,44,13,22,55,66,77]

print("Supermarket")
print("===========")

total = 0

while True:
    choice = int(input("Please select product (1-10) 0 to Quit: "))
    if choice == 0:
        break
    total += prices[choice - 1]
    print("Product:", choice, "Price:", prices[choice - 1])

print("Total:", total)
payment = int(input("Payment: "))
print("Change:", payment - total)
