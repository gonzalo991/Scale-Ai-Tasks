class Address:
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country

    def get_address(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"