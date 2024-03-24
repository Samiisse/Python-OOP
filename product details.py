#Given a CSV file with product details (name, price, quantity), create a Product class to manage the data

import csv

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"

# Function to read product data from CSV file
def read_product_data(csv_file):
    products = []
    try:
        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(row['Name'], float(row['Price']), int(row['Quantity']))
                products.append(product)
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print("Invalid CSV format. Missing required fields.")

    return products

# Example usage:
csv_file = input("Enter the path of the CSV file: ")
product_data = read_product_data(csv_file)
for product in product_data:
    print(product)
