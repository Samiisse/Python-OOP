#Given a JSON file with customer data, create a Customer class to store and manipulate the data

import json

class Customer:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Age: {self.age}"

# Function to read customer data from JSON file
def read_customer_data(json_file):
    customers = []
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            for entry in data['customers']:
                customer = Customer(entry['name'], entry['email'], entry['age'])
                customers.append(customer)
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Invalid JSON format. Missing required fields.")

    return customers

# Example usage:
json_file = input("Enter the path of the JSON file: ")
customer_data = read_customer_data(json_file)
for customer in customer_data:
    print(customer)
