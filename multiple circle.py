#Implement a program that uses a Circle class to calculate the area and circumference of multiple circles

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
def calculate_circle_properties(radius):
    circle = Circle(radius)
    area = circle.calculate_area()
    circumference = circle.calculate_circumference()
    return area, circumference

# Input the number of circles
num_circles = int(input("Enter the number of circles: "))

# Input radius for each circle and calculate properties
for i in range(num_circles):
    radius = float(input(f"Enter the radius of circle {i+1}: "))
    area, circumference = calculate_circle_properties(radius)
    print(f"Circle {i+1} - Area: {area}, Circumference: {circumference}")
