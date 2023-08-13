from User import User
from Librarian import Librarian
from Book import Book
from Library import Library

# Create a librarian
librarian = Librarian("Juan", "Cruz")

# Create a library
library = Library("Athenas Library", librarian, "456 Junin St")

# Create a book
book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)

# Add the book to the library
library.add_book(book)

# Create a user
user = User("Gonzalo", "Ara", "A12345")

# Add the user to the library
library.add_user(user)

book_to_borrow = "The Great Gatsby"
 
# User borrows a book from the library
borrowed_book = user.borrow_book(book_to_borrow)

# Print the borrowed book
print(borrowed_book)

# Print the user's borrowed books
print(f"{user.get_name()} has borrowed: {book_to_borrow}")

# Print the library's books
print(f"{library.name} has the following books: {', '.join([book.get_title() for book in library.get_books()])}")