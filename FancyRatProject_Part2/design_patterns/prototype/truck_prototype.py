from abc import ABC, abstractmethod

# Define a base class for Truck objects
class Truck(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def clone(self):
        pass

    # String representation of the Truck object
    def __repr__(self):
        return f"{self.__class__.__name__}(Make: {self.make}, Model: {self.model}, Year: {self.year})"

# Subclass for Truck, inheriting from Truck
class ConcreteTruck(Truck):
    def __init__(self, make, model, year, cargo_capacity):
        super().__init__(make, model, year)
        self.cargo_capacity = cargo_capacity

    # Override the clone method for Truck
    def clone(self):
        new_truck = ConcreteTruck(self.make, self.model, self.year, self.cargo_capacity)
        return new_truck

    # String representation of the Truck object
    def __repr__(self):
        return f"{super().__repr__()}, Cargo Capacity: {self.cargo_capacity}"

# Create a truck prototype
truck = ConcreteTruck("Ford", "F-150", 2022, 1000)
another_truck = truck.clone()

# Clone the truck prototype to create a new truck
new_truck = ConcreteTruck("Chevrolet", "Silverado", 2023, 1500)
another_new_truck = new_truck.clone()

# Print the prototype and cloned truck objects with their details
print("Truck Prototype:")
print(truck)
print(another_truck)

print("\nCloned Truck:")
print(new_truck)
print(another_new_truck)