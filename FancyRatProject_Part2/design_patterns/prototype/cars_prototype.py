from abc import ABC, abstractmethod
# Define a base class for Car objects
class Car(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def clone(self):
        pass

    # String representation of the Car object
    def __repr__(self):
        return f"{self.__class__.__name__}(Make: {self.make}, Model: {self.model})"
    
# Subclass for SportsCar, inheriting from Car
class SportsCar(Car):
    def __init__(self, make, model, engine_power):
        super().__init__(make, model)
        self.engine_power = engine_power

    # Override the clone method for SportsCar
    def clone(self):
        new_car = SportsCar(self.make, self.model, self.engine_power)
        return new_car

    # String representation of the SportsCar object
    def __repr__(self):
        return f"{super().__repr__()}, Engine Power: {self.engine_power}"

# Subclass for Sedan, inheriting from Car
class Sedan(Car):
    def __init__(self, make, model, passengers):
        super().__init__(make, model)
        self.passengers = passengers

    # Override the clone method for Sedan
    def clone(self):
        new_car = Sedan(self.make, self.model, self.passengers)
        return new_car

    # String representation of the Sedan object
    def __repr__(self):
        return f"{super().__repr__()}, Passengers: {self.passengers}"

# Subclass for SUV, inheriting from Car
class SUV(Car):
    def __init__(self, make, model, cargo_space):
        super().__init__(make, model)
        self.cargo_space = cargo_space

    # Override the clone method for SUV
    def clone(self):
        new_car = SUV(self.make, self.model, self.cargo_space)
        return new_car

    # String representation of the SUV object
    def __repr__(self):
        return f"{super().__repr__()}, Cargo Space: {self.cargo_space}"

# Create a sports car prototype
sports_car = SportsCar("Toyota", "Camry", 700)
another_sport_car = sports_car.clone()

# Clone the sports car prototype to create a new car (sedan)
sedan = Sedan("Chevrolet", "Malibu", 5)
another_sedan = sedan.clone()

# Clone the sports car prototype to create another new car (SUV)
suv = SUV("Ford", "Escape", 200)
another_suv = suv.clone()

# Print the prototype and cloned car objects with their details
print("Sports Car Prototype:")
print(sports_car)
print(another_sport_car)

print("\nCloned Sedan:")
print(sedan)
print(another_sedan)

print("\nCloned SUV:")
print(suv)
print(another_suv)