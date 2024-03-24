#Create a class to represent a basic calculator with add, subtract, multiply, and divide methods.

class BasicCalculator:
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2
    
    def multiply(self, num1, num2):
        return num1 * num2
    
    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

# Example usage:
calculator = BasicCalculator()
result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(5, 3)
result_multiply = calculator.multiply(5, 3)
result_divide = calculator.divide(5, 3)

print("Addition result:", result_add)
print("Subtraction result:", result_subtract)
print("Multiplication result:", result_multiply)
print("Division result:", result_divide)

