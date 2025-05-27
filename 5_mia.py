# Typecasting = the process of converting variable of one data type to another is called.
# str(), int(), float(), bool()

name = "Bruh"
name3 = ""
age = 23
gpa = 3.42
is_students = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_students))

name = bool(name) # gives true
name3 = bool(name3) # gives false
# we could use this method where we have to enter names. if someone
# doesn't use name, put the field in blank we could easily find
# that bcz we will get false and we can again ask the person to re-enter.

print(name)
print(name3)
print(type(name),type(name3))

age = float(age)
gpa = int(gpa)

print(age, gpa)
print(type(age), type(gpa))

age = int(age)
age = str(age)
'''
age += 1
print(age) it will give error bcz now age = 23 is str.
so we can't add a number to a string
'''
age += '1'
print(age) 
# as age is now an str so with + which will concatenate str 1 with 
# str 23 and that is 231
