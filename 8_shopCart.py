item = input("Which item would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like to buy?: "))
total = price * quantity

print(f"You have bought: {quantity} x {item}'s.")
print(f"Total Price: MRP-{total} TK")