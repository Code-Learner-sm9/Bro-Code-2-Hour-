'''input() = A function that promts the user to enter data

In python whatever data is given through the user returned as
string.'''

name = input("What is your data: ")
age = int(input("How old are you: "))

# age = int(age) we can do like these or direct declare typecast
# at input()
age = age + 1 # as input() function in python takes number as str
# so we have to typecast the numbers to int

# If your are going to insert variable in a string use f_string.
print(f"Hello {name}!") 
print("Happy Birthday.")
print(f"You are {age} years old.")