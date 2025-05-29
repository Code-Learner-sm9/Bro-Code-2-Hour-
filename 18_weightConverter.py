# Weight Converter Program
# if weight is in kg then convert it in lb and vice versa
weight = float(input("Enter Your Weight: "))
unit = input("Kilogram or Pound(K or L): ")

if unit == "K":
  weight = weight / 2.205
  unit = "Lbs"
  print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
  weight = weight * 2.205
  unit = "Kg"
  print(f"Your weight is: {round(weight, 2)} {unit}")
else:
  print("Invalid Request.")
