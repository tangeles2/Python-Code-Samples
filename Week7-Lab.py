# Tony Angeles
# 11.10.24

# Problem 1
import math
def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area
result = calculate_circle_area(10)
print("The area of the cirlce is", result)

# Problem 2
def check_in_range(num):
    if num in range(1, 10):
        print(f"{num} is in range")
    else:
        print(f"{num} is not in range")
check_in_range(5)
check_in_range(15)

# Problem 3
from functools import reduce
def multiply_list(lst):
    result = reduce((lambda x,y: x*y),lst)
    return result
sample_list= [5,2,7,-1]
print(multiply_list(sample_list))

# Problem 4
def unique_list(numbers) :
    unique = []
    for item in numbers :
        if item not in unique:
            unique.append(item)
        return list(set(numbers))
print(unique_list([1,3,3,3,6,2,3,5]))

# Problem 5
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
drawSquare(alex, 100)

wn.exitonclick()

# Problem 6
class car:
    def __init__(self, model, year,color, type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer
    def get_model(self):
        return self.model
    def get_year(self):
        return self.year
    def get_color(self):
        return self.color
    def get_type(self):
        return self.type
    def get_manufacturer(self):
        return self.manufacturer
    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + str(self.type) + ' ' + self.manufacturer
car1 = car("Sports", 2012, "Blue", "small","Porsche")
car2 = car("Sedan", 2020, "Black", "medium", " Nissan")
print(car1.fullspecs())
print(car2.fullspecs())


