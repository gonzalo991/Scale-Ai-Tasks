class House:
    def __init__(self, address, bedroom, bathroom, diningroom, living):
        self._address = address
        self._bedroom = bedroom
        self._bathroom = bathroom
        self._diningroom = diningroom
        self._living = living

    def __str__(self) -> str:
        return f"Address: {self._address} , Bedroom: [ {self._bedroom} ],\n Bathroom: [ {self._bathroom} ], Diningroom: [ {self._diningroom} ], Livingroom: [ {self._living} ]"

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, new_address):
        self._address = new_address
