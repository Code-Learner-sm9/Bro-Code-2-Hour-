# if else

age = int(input("Enter Your Age to Signed UP: "))

if age >= 100:
  print("You are too old to sign up!")
elif age <= 0:
  print("You haven't borned yet!")
elif age >= 18:
  print("You are already signed up.")
else:
  print("You have to be at least 18 to be signed up.")