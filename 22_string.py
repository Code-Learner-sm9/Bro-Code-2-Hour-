# string functions

name = input("Enter your full name: ")

# The lenght of the name. it counts the blank space too.
result = len(name)
print(result)

# Finds a charater in a string returns the indexed number. it counts from 0, if it doesn't find the charater it'll return -1

results = "S.M. Shahidul Alam"
result = results.find("M")
print(result)

# In my name there are three A's so if i want to find the last A 
result = results.rfind("a")
print(result)

# To Capitalize the first char of a sentence
result = results.capitalize()
print(result)

# Convert all the characters to uppercase
result = results.upper()
print(result)

# Convert all the characters to lowercase
result = results.lower()
print(result)

# Check whether the given name contains all alphabets or not, here digits are not allowed, name containing digit also not allowed, name containing spaces also not allowed
# It returns the result in boolean true or false

nam = "Shahidul"
nam1 = "Shahidul123"
nam2 = "Shahidul Alam"
nam3 = "123"
result1 = nam.isalpha()
result2 = nam1.isalpha()
result3 = nam2.isalpha()
result4 = nam3.isalpha()

print(result1, result2, result3, result4)


# check whether the given name contains digits or not and returns boolean values.

namee = "123"
result = namee.isdigit()
print(result)

# count character, numbers in a given string

phone = "1-1234-434-567-987-88"
result = phone.count("-")
result1 = phone.count("1")

print(f"'-' are in total {result} and '1' are in total {result1}")

# replace characters
result = phone.replace("8", "x")
print(result)

