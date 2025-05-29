# conditional expression = a one line shortcut for the if-else statement (similar to ternary operator)

num = 4

print("Positive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)

a = 3
b =8
max_num = a if a>b else b
print(max_num)
 
min_num = a if a<b else b
print(min_num)

age = "Adult" if num >= 18 else "Boy"
print(age)

temp1 = 18
temp = "Hot" if temp1 > 25 else "Cold"
print(temp)

passw = "admin"
access_level = "Full Access" if passw == "admin" else "Limited Access"
print(access_level)