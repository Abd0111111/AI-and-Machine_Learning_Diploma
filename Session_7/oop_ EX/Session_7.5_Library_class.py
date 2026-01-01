# The code below shows how to keep title and author inside each book object
# It explains how to add book objects to the library list
# It explains how to print all stored books using a loop
# You can use this structure in simple systems that track items with basic relationships

class Book:
    def __init__(self, title, author):     # creates a book with title and author
        self.title = title                 # saves title
        self.author = author               # saves author

    def display(self):                     # shows book data
        print(f"Title: {self.title}, Author: {self.author}")  # prints title and author

class Library:
    def __init__(self):                    # creates an empty library
        self.books = []                    # stores all book objects

    def add_book(self, book):              # adds a book object
        self.books.append(book)            # pushes book into the list
        print(f"Added book: {book.title}") # prints added book title

    def list_books(self):                  # lists all books
        print("Library books:")            # header
        for book in self.books:            # loops through books
            book.display()                 # prints book data

# Example usage
book1 = Book("1984", "George Orwell")                # creates first book
book2 = Book("To Kill a Mockingbird", "Harper Lee")  # creates second book
library = Library()                                   # creates library
library.add_book(book1)                               # adds first book
library.add_book(book2)                               # adds second book
library.list_books()                                  # prints all books