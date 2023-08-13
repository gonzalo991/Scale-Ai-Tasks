class Librarian:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_name(self):
        return f"{self.name} {self.surname}"

    def introduce(self):
        return f"Hi, my name is {self.name} {self.surname} and I'm the librarian here"