# to check whether you entered int or float number. 
# and do an operation.
import math
print("Welcome to number identifier tool: \n\n")
# \n for new line.

user_input = input("Enter a number: ")


try: 
  #if the entered number is integer:
  number = int(user_input) # in try method checks whether the entered
  # number is int type or not
  print(f"Your entered number: {user_input} is int type.")
  print(f"The square of {user_input} is: {pow(number, 2)}")
except ValueError:
  print("Invalid Input typped.")

try:
  number = float(user_input)
  print(f"Your entered number: {user_input} is float type.")
  print(f"The squre root of {user_input} is: {round(math.sqrt(number), 3)}") # round(operation, 3) means 3 numbers after dot.
except ValueError:
  print("Invalid Input typped.")

# In Python, the pass statement is a placeholder. It does nothing when executed — it's used when a statement is syntactically required but you don’t want any code to run.
try:
  # if we normally put these into blank state then it would give us an error but as we put pass statement so we can put it in a blank state for now.
  pass
except ValueError:
  pass

