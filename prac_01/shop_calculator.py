"""
CP1404/CP5632 - Practical
Shop calculator program to determine total price with potential discount
"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for num in range(1, number_of_items + 1):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price

if total_price > 100:
    total_price = total_price * 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

