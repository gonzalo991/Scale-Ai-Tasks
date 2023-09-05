from abc import ABC, abstractmethod

# Hotel class
class Hotel(ABC):
    # Dunder init method
    def __init__(self, name, address, star_rating, rooms):
        self._name = name
        self._address = address
        self._star_rating = star_rating
        self._rooms = rooms

    #Dunder str method
    def __str__(self) -> str:
        return f" Name: {self._name}, Address: {self._address}, Star Rating: {self.star_rating}, Rooms: {self.rooms}"
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
    def __init__(self, guest_id, name, room_number):
        self._guest_id = guest_id
        self._name = name
        self._room_number = room_number

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

# Budget Hotel class
class BudgetHotel(Hotel):
    def __init__(self, name, address, star_rating, rooms):
        super().__init__(name, address, star_rating, rooms)

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
    def calculate_cost(self, nights_number, guests):
        return 200 * nights_number + 80 * guests

    # abstract method to book a room
    def book_room(self, guest_data, guests, nights_number):
        total_cost = self.calculate_cost(nights_number, guests)
        print(f"Room booked at {self.name} for {guests} guests for {nights_number} nights.")
        print(f"Total cost: ${total_cost}")
        print(f"Guest details: [ Guest Name: {guest_data.name}, Guest Room: {guest_data.room_number}, Guest ID: {guest_data.guest_id} ]")

# Example usage
guest1 = Guest(1, "Gonzalo", 14)
budget_hotel = BudgetHotel("Budget Hotel", "123 Main St", 10, 70)
budget_hotel.calculate_cost(2, 5)
budget_hotel.book_room(guest1, 5, 2)

# LuxuryHotel class
class LuxuryHotel(Hotel):
    # dunder init method
    def __init__(self, name, address, star_rating, rooms, spa, restaurant, safe_box):
        super().__init__(name, address, star_rating, rooms)
        self._spa = spa
        self._restaurant = restaurant
        self._safe_box = safe_box

    # dunder str method
    def __str__(self) -> str:
        return f"Luxury Hotel: [ {super().__str__()}, Spa: {self._spa}, Restaurant: {self._restaurant}, Safe Box: {self._safe_box}]"

    # Getters and Setters for additional attributes
    @property
    def spa(self):
        return self._spa
    
    @spa.setter
    def spa(self, spa):
        self._spa = spa

    @property
    def restaurant(self):
        return self._restaurant
    
    @restaurant.setter
    def restaurant(self, restaurant):
        self._restaurant = restaurant

    @property
    def safe_box(self):
        return self._safe_box
    
    @safe_box.setter
    def safe_box(self, safe_box):
        self._safe_box = safe_box

    def calculate_cost(self, nights_number, guests):
        return 300 * nights_number + 100 * guests

    def book_room(self, guest_data, guests, nights_number):
        total_cost = self.calculate_cost(nights_number, guests)
        print(f"Room booked at {self.name} for {guests} guests for {nights_number} nights.")
        print(f"Total cost: ${total_cost}")
        print(f"Guest details: [ Guest Name: {guest_data.name}, Guest Room: {guest_data.room_number}, Guest ID: {guest_data.guest_id} ]")

# Example usage
guest1 = Guest(1, "Gonzalo", 14)
luxury_hotel = LuxuryHotel("Palace Hotel", "123 Main St", 10, 70, True, True, True)
print(luxury_hotel)
luxury_hotel.calculate_cost(2, 5)
luxury_hotel.book_room(guest1, 5, 2)