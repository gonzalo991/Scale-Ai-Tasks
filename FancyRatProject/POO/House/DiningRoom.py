# Create the dining room class
class DiningRoom:
    # Define the dunder init method
    def __init__(self, dining_table, chairs, refrigerator, sink):
        self._dining_table = dining_table
        self._chairs = chairs
        self._refrigerator = refrigerator
        self._sink = sink

    # Define the dunder str method to display the details of the class
    def __str__(self) -> str:
        return f"[ Dining Table: {self._dining_table}, Chairs: {self._chairs}, Refrigerator: {self._refrigerator}, Sink: {self._sink} ]"

    # Define getters and setter with the @property annotation
    @property
    def dining_table(self):
        return self._dining_table

    @dining_table.setter
    def dining_table(self, new_dining_table):
        self._dining_table = new_dining_table

    @property
    def chairs(self):
        return self._chairs

    @chairs.setter
    def chairs(self, more_chairs):
        self._chairs = more_chairs

    @property
    def refrigerator(self):
        return self._refrigerator

    @refrigerator.setter
    def refrigerator(self, new_refrigerator):
        self._refrigerator = new_refrigerator

    @property
    def sink(self):
        return self._sink

    @sink.setter
    def sink(self, new_sink):
        self._sink = new_sink

# Example of usage

# Define a new Dining Room class
my_dining_room = DiningRoom(True, 4, True, True)

# Print the details of the dining room
print(my_dining_room) # [ Dining Table: True, Chairs: 4, Refrigerator: True, Sink: True ]