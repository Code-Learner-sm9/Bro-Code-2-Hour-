# circumference of circle 2*pi*r (r = radius)

import math

radius = float(input("Enter Radius: "))

print(f"Circumference of Circle: {round(2*math.pi*radius, 3)}")

#round(result) # rounds the result
#round(result, 2) # rounds the result if it is floating point 2 means
# after dot it will take 2 digits


# Area of a circle: Area = pi*r^2

print(f"Area of a Circle: {round(math.pi*pow(radius, 2), 2)}")

# hypotenuse of a triangle: hypotenuse, c = sqrt(a^2, b^2)
# if a triangle has 3 arms then hypotenuse is the biggest arm
# a = 3 , b = 4 then c = 5. so c is hypotenuse

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print(f"The hypotenuse(c) of the triangle is: {round(math.sqrt(pow(a,2) + pow(b,2)))}")
