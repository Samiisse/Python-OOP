#Create a class to represent a Car with attributes like make, model, and year

class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

# Example usage:
make = input("Enter car's make: ")
model = input("Enter care's model: ")
year = int(input("Enter car's year: "))


car = car(make, model, year)
print("Car details:")
print(car)