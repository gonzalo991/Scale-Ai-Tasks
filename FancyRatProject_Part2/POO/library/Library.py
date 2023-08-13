class Library:
    def __init__(self, name, librarian, address):
        self.name = name
        self.librarian = librarian
        self.address = address
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)

    def get_books(self):
        return self.books

    def get_users(self):
        return self.users