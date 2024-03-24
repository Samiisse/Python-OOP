#Create a class to represent a book with attributes like title, author, and publication year.

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

# Example usage:
book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print("Book 1:", book1)
print("Book 2:", book2)

