#ifs

print("Welcome to 1st Ex: ")
response = input("Would you like some food?(Y/N): ")

# == is comparison operator and = is assignment operator.
if response == "Y":
  print("Have some food.")
else: 
  print("NO food for you.")

print("Welcome to 2nd Ex: ")

name = input("Enter your name: ")

if name == "":
  print("You haven't entered your name.")
else: 
  print(f"Hello, {name}")

print("Welcome to 3rd Ex: ")
#ifs with boolean

for_sale = True

if for_sale:
  print("The item is for sale.")
else: 
  print("The item isn't for sale.")

print("Welcome to 4th Ex: ")

status = False

if status:
  print("You are online.")
else:
  print("You are offline.")

print("Completed.")


