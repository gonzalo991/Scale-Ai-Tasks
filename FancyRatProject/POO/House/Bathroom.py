# Create the bathroom class
class Bathroom:
    # Define the dunder init method
    def __init__(self, toilet, bathtub, sink, shower, toilet_seat, medicine_cabinet, towel_rack):
        self._toilet = toilet
        self._bathtub = bathtub
        self._sink = sink
        self._shower = shower
        self._toilet_seat = toilet_seat
        self._medicine_cabinet = medicine_cabinet
        self._towel_rack = towel_rack

    # Define the dunder str method to display the details of the class
    def __str__(self) -> str:
        return f"[ Toilet: {self._toilet}, Bathtub: {self._bathtub}, Sink: {self._sink}, Shower: {self._shower}, Toilet Seat: {self._toilet_seat}, Medicine Cabinet: {self._medicine_cabinet}, Towel Rack: {self._towel_rack} ]"

    # Define getters and setter with the @property annotation
    @property
    def toilet(self):
        return self._toilet

    @toilet.setter
    def toilet(self, new_toilet):
        self._toilet = new_toilet

    @property
    def bathtub(self):
        return self._bathtub

    @bathtub.setter
    def bathtub(self, new_bathtub):
        self._bathtub = new_bathtub

    @property
    def sink(self):
        return self._sink

    @sink.setter
    def sink(self, new_sink):
        self._sink = new_sink

    @property
    def shower(self):
        return self._shower

    @shower.setter
    def shower(self, new_shower):
        self._shower = new_shower

    @property
    def toilet_seat(self):
        return self._toilet_seat

    @toilet_seat.setter
    def toilet_seat(self, new_toilet_seat):
        self._toilet_seat = new_toilet_seat

    @property
    def medicine_cabinet(self):
        return self._medicine_cabinet

    @medicine_cabinet.setter
    def medicine_cabinet(self, new_medicine_cabinet):
        self._medicine_cabinet = new_medicine_cabinet

    @property
    def towel_rack(self):
        return self._towel_rack

    @towel_rack.setter
    def towel_rack(self, new_towel_rack):
        self._towel_rack = new_towel_rack

# Example of usage

# Define a new Bathroom class
my_bathroom = Bathroom(True, True, True, True, True, True, True)

# Print the details of the bathroom
print(my_bathroom) # [ Toilet: True, Bathtub: True, Sink: True, Shower: True, Toilet Seat: True, Medicine Cabinet: True, Towel Rack: True 
