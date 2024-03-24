#Write a program that uses a Person class to keep track of a person's name, age, and address

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

# Example usage:
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
address = input("Enter person's address: ")

person = Person(name, age, address)
print("Person details:")
print(person)
