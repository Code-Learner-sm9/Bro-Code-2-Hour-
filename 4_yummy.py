# Variable = A container for a value (String, integer, boolean, float)

# Strings (A Series of Characters) In a string bruh123 are also 
# recognized as string. Everything within a double quote is a string.
first_name = "Labid"
email = "bruh123@fake.com"
print(first_name)

#print using f-string (f for format)
print(f"Heelo {first_name}")
# Multiple 
print(f"{first_name} Email is: {email} {first_name}")


#Integers
age = 27
num = 30
print(f"You are {age} years old")
print(f"There are {num} students in our class")

#Float 
price= 34.5
gpa=3.45
distance=8.3

print(f"Total price is ${price}")
print(f"You've got {gpa} GPA")
print(f"The town is about {distance}km away")

# Boolean
is_students = True
is_sale = False

if is_students:
  print("The students are attentive.")
else:
  print("The students are not attentive.")

if is_sale:
  print("The sales are open today.")
else:
  print("The sales are not open today.")