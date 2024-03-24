#Write a Python program that uses a Rectangle class to calculate the area and perimeter of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rectangle = Rectangle(length, width)
area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Area of the rectangle: {area}")
print(f"Perimeter of the rectangle: {perimeter}")
