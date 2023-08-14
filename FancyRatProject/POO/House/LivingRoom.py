# Create the living room class
class LivingRoom:
    # Define the dunder init method
    def __init__(self, sofa, television, fireplace, coffee_table, plants, computer, library):
        self._sofa = sofa
        self._television = television
        self._fireplace = fireplace
        self._coffee_table = coffee_table
        self._plants = plants
        self._computer = computer
        self._library = library

    # Define the dunder str method to display the details of the class
    def __str__(self) -> str:
        return f"[ Sofa: {self._sofa}, Television: {self._television}, Fireplace: {self._fireplace}, Coffee Table: {self._coffee_table}, Plants: {self._plants}, Computer: {self._computer}, Library: {self._library} ]"

    # Define getters and setter with the @property annotation
    @property
    def sofa(self):
        return self._sofa

    @sofa.setter
    def sofa(self, new_sofa):
        self._sofa = new_sofa

    @property
    def television(self):
        return self._television

    @television.setter
    def television(self, new_television):
        self._television = new_television

    @property
    def fireplace(self):
        return self._fireplace

    @fireplace.setter
    def fireplace(self, new_fireplace):
        self._fireplace = new_fireplace

    @property
    def coffee_table(self):
        return self._coffee_table

    @coffee_table.setter
    def coffee_table(self, new_coffee_table):
        self._coffee_table = new_coffee_table

    @property
    def plants(self):
        return self._plants

    @plants.setter
    def plants(self, new_plants):
        self._plants = new_plants

    @property
    def computer(self):
        return self._computer

    @computer.setter
    def computer(self, new_computer):
        self._computer = new_computer

    @property
    def library(self):
        return self._library

    @library.setter
    def library(self, new_library):
        self._library = new_library

# Example of usage
# Define a new Living Room class
my_living_room = LivingRoom(True, 2, True, True, 5, 1, False)

# Print the details of the living room
print(my_living_room) # [ Sofa: True, Television: 2, Fireplace: True, Coffee Table: True, Plants: 5, Computer: 1, Library: False ]