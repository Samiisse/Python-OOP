#Given a CSV file with employee details (name, position, salary), create a class to represent an Employee3

import csv

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}"

# Example usage:
def read_employee_csv(csv_file):
    employees = []
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['Name']
                position = row['Position']
                salary = float(row['Salary'])
                employees.append(Employee(name, position, salary))
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error: Unable to convert salary to float.")
    return employees

# Example usage:
csv_file = input("Enter the path of the CSV file: ")
employees = read_employee_csv(csv_file)
for employee in employees:
    print(employee)
