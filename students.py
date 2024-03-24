#Create a class to represent a Student with attributes like name, age, and grades

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}"

# Example usage:
name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
grades = input("Enter student's grades (comma-separated): ").split(',')
grades = [float(grade.strip()) for grade in grades]  # Convert grades to float

student = Student(name, age, grades)
print("Student details:")
print(student)
