#Create a class to represent a Movie with attributes like title, director, and rating.

class Movie:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating
    
    def __str__(self):
        return f"Title: {self.title}, Director: {self.director}, Rating: {self.rating}"

# Example usage:
movie1 = Movie("Inception", "Christopher Nolan", "PG-13")
movie2 = Movie("The Shawshank Redemption", "Frank Darabont", "R")
movie3 = Movie("The Godfather", "Francis Ford Coppola", "R")

print("Movie 1:", movie1)
print("Movie 2:", movie2)
print("Movie 3:", movie3)
