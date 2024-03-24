#Define a class for a Circle with methods to calculate its area and circumference.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

# Example usage:
radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)

area = circle.calculate_area()
circumference = circle.calculate_circumference()

print("Area of the circle:", area)
print("Circumference of the circle:", circumference)
