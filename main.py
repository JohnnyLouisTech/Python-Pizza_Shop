# Python pizza store
# What we'll be collecting from our customers and greetings
print("Welcome to Python Pizza Deliveries Shop!")
size = input("What would you like for size? S, M, or L ")
add_pepperoni = input("Do you want to add pepperoni? Y or N ")
extra_cheese = input("Do you to add extra cheese? Y or N ")

# Start of the order
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
if size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2

if add_pepperoni == "Y":
    if size == "M" or "L":
        bill += 3

if extra_cheese == "Y":
    bill += 1.50

# End of the order where we'll print the total bill to the customer

print(f"Your final bill is: ${bill}. ")
print(f"Please, visit us again soon!.")
