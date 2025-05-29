# calculator

print("Welcome to HomeMade Calculator: ")

operator = input("Enter an operator(+ - * /): ")

num1 = float(input("\n\nEnter 1st number: "))
num2 = float(input("Enter 2nd number: "))

if operator == "+":
  result = num1 + num2
  print(f"The result is: {round(result)}")
elif operator == "-":
  result = num1 - num2
  print(f"The reslut is: {round(result)}")
elif operator == "*":
  result = num1 * num2
  print(f"The result is: {round(result)}")
elif operator == "/":
  result = num1 / num2
  print(f"The result is: {round(result, 3)}")
elif operator == "":
  print("You haven't entered any operator.")
else:
  print("Invalid operator.")