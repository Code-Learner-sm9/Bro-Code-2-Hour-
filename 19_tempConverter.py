# Temperature Converter.

unit = input("Is this temperature in celcius or farenhite(C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
  temp = round((9 * temp) / 5 + 32, 1)
  print(f"The temperature now: {temp}°F") # alt + from numpad(0176) for the degree sign.
elif unit == "F":
  temp = round(((temp - 32) * 5 / 9), 1)
  print(f"The temperature now: {temp}°C")
else:
  print(f"{unit} is Invalid.")