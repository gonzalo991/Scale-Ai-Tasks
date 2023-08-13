class User:
    def __init__(self, name, surname, library_code):
        self.name = name
        self.surname = surname
        self.library_code = library_code
        self.borrowed_books = []

    def get_name(self):
        return f"{self.name} {self.surname}"

    def borrow_book(self, book_title):
        self.borrowed_books.append(book_title)
        return f"{self.get_name()} borrowed: {book_title}"

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            self.borrowed_books.remove(book_title)
            return f"{self.get_name()} returned '{book_title}'."
        else:
            return f"{self.get_name()} did not borrow '{book_title}'."