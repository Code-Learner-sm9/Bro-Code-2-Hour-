# Logical Operator = evaluates multipal operations(and, or, not)

# and operator = at least one condition must be true
# or operator = both conditions should be true
# not operator = inverts the condition (not false, not true)

temp = int(input("Enter the temperature: "))
is_sunny = False
is_raining = True

if temp > 32 and is_sunny:
  print("It's Hot today.")
  print("It is Sunny today.")

elif 32 > temp > 20 and is_sunny:
  print("It's a better weather today.")
  print("It's Sunny today.")

elif temp > 32 or is_sunny:
  print("It's Hot today.")
  print("It is Sunny today.")

elif 16 > temp > 0 and is_raining and not is_sunny:
  print("It's cloudy today.")  
  print("It's raining outside.")

else:
  print("Invalid Output.")
