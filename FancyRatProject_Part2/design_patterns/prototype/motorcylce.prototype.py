from abc import ABC, abstractmethod
from copy import deepcopy
from typing import List, Optional

# Define a base class for motorcycles
class Motorcycle(ABC):
    @abstractmethod
    def clone(self) -> 'Motorcycle':
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(Make: {self.make}, Model: {self.model})"

# Define a subclass for sports motorcycles
class SportsMotorcycle(Motorcycle):
    def __init__(self, make: str, model: str, engine_power: int):
        self.make = make
        self.model = model
        self.engine_power = engine_power

    def clone(self) -> 'Motorcycle':
        new_motorcycle = deepcopy(self)  # Create a deep copy to ensure independent instances
        return new_motorcycle

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Engine Power: {self.engine_power}"

# Define a subclass for cruiser motorcycles
class CruiserMotorcycle(Motorcycle):
    def __init__(self, make: str, model: str, passengers: int):
        self.make = make
        self.model = model
        self.passengers = passengers

    def clone(self) -> 'Motorcycle':
        new_motorcycle = deepcopy(self)  # Create a deep copy to ensure independent instances
        return new_motorcycle

    def __repr__(self) -> str:
        return f"{super().__repr__()}, Passengers: {self.passengers}"

# Create a sports motorcycle prototype
sports_motorcycle = SportsMotorcycle("Yamaha", "R1", 500)
another_sports_motorcycle = sports_motorcycle.clone()

# Clone the sports motorcycle prototype to create a new motorcycle (cruiser)
cruiser_motorcycle = CruiserMotorcycle("Harley-Davidson", "Street Glide", 2)
another_cruiser_motorcycle = cruiser_motorcycle.clone()

# Print the details of the prototype and cloned motorcycle objects
print("Sports Motorcycle Prototype:")
print(sports_motorcycle)
print(another_sports_motorcycle)

print("\nCruiser Motorcycle:")
print(cruiser_motorcycle)
print(another_cruiser_motorcycle)
