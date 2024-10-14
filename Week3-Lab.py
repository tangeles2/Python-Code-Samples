# Tony Angeles
# 10.13.24

# Problem 1
print ("Hello World")
# Problem 2
first_name = input(" Enter your first name: ")
print ( "Hello", first_name)
# Problem 3
Student = input("Enter student name: ")
Instructor = input("Enter instructor name: ")
print ( "Hello", Student, "Hello", Instructor)
# Problem 4
from math import pi
r = float(input("input the radius of the circle: "))
area = pi * r**2
print("The area of the circle with radius " + str(r) +  " is: " + str(area))
# Problem 5
m= (int(input("Enter number of miles driven: ")))
g= (int(input("Enter number of gallons: ")))
print(str(m) + "miles per " + str(g) + "gallons")
# Problem 6
temperature = float(input("Please enter your temperature in fahrenheit: "))
celsius = (temperature - 32) * 5/9
print("Temperature in celsius: " , celsius)
# Problem 7
start_day= input("Enter starting day number: ")
length= input("Enter length of stay: ")
final= (int(start_day) + int(length))%7
print(final)
