# Import dependencies
from abc import ABC, abstractmethod

# Hotel class
class Hotel(ABC):
    # Dunder init method
    def __init__(self, name, address, star_rating, rooms):
        self._name = name
        self._address = address
        self._star_rating = star_rating
        self._rooms = rooms

    # Dunder str method
    def __str__(self) -> str:
        return f"Hotel: [ Name: {self._name}, Address: {self._address}, Star Rating: {self._star_rating}, Rooms: {self._rooms} ]"

    # Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def star_rating(self):
        return self._star_rating
    
    @star_rating.setter
    def star_rating(self, star_rating):
        self._star_rating = star_rating

    @property
    def rooms(self):
        return self._rooms
    
    @rooms.setter
    def rooms(self, rooms):
        self._rooms = rooms

    # abstract method to calculate the room's cost
    @abstractmethod
    def calculate_cost(self, nights_number, guests):
        pass
 
    # abstract method to book a room
    @abstractmethod
    def book_room(self, guest_data, guests, nights_number):
        pass

# Guest class
class Guest:
    # Dunder init method for guest class
    def __init__(self, guest_id, name, room_number):
        self._guest_id = guest_id
        self._name = name
        self._room_number = room_number

    # Dunder str method for Guest
    def __str__(self) -> str:
        return f"Guest ID: {self._guest_id}, Guest Name: {self._name}, Room Number: {self._room_number}"

    # Getters and Setters
    @property
    def guest_id(self):
        return self._guest_id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def room_number(self):
        return self._room_number
    
    @room_number.setter
    def room_number(self, room_number):
        self._room_number = room_number

# Balcony Hotel class
class BalconyHotel(Hotel):
    # Dunder init method
    def __init__(self, name, address, star_rating, rooms, balcony):
        super().__init__(name, address, star_rating, rooms)
        self._balcony = balcony

    # Dunder str method
    def __str__(self) -> str:
        return f"{super().__str__()}, Balcony: {self._balcony}"
    
    # Getters and Setters for additional attributes
    @property
    def balcony(self):
        return self._balcony
    
    @balcony.setter
    def balcony(self, balcony):
        self._balcony = balcony

    def calculate_cost(self, nights_number, guests):
        return 275 * nights_number + 125 * guests

    def book_room(self, guest_data, guests, nights_number):
        total_cost = self.calculate_cost(nights_number, guests)
        print(f"Room booked at {self.name} for {guests} guests for {nights_number} nights.")
        print(f"Total cost: ${total_cost}")
        print(f"Guest details: [ Guest Name: {guest_data.name}, Guest Room: {guest_data.room_number}, Guest ID: {guest_data.guest_id} ]")

# Example usage
guest1 = Guest(1, "Gonzalo", 14)
balcony_hotel = BalconyHotel("Balcony Hotel", "123 Main St", 4, 70, True)
print(balcony_hotel)
balcony_hotel.calculate_cost(2, 5)
balcony_hotel.book_room(guest1, 5, 2)