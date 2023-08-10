from abc import ABC, abstractmethod

class Motorcycle(ABC):
    def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
        self.color = color
        self.license_plate = license_plate
        self.fuel_liters = fuel_liters
        self.wheel_number = wheel_number
        self.brand = brand
        self.model = model
        self.date_made = date_made
        self.top_speed = top_speed
        self.weight = weight
        self.engine = engine
        self.displacement = displacement
        self.price = price

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def is_running(self):
        return self.engine == "on"

    def motorcycle_price(self):
        return self.price

    def motorcycle_fuel_left(self):
        return self.fuel_liters
    
    def max_fuel_capacity(self, fuel):
        capacity = self.fuel_liters + fuel
        if capacity <= 20:
            self.fuel_liters = capacity
            return f"The fuel tank now has: {self.fuel_liters} liters."
        else:
            return f"Invalid quantity of fuel: {fuel}. Exceeds maximum capacity of 20 liters."

    def getDetails(self):
        return f"Color: {self.color}, License Plate: {self.license_plate}, Left Fuel: {self.fuel_liters}, Brand: {self.brand}, Model: {self.model}, Date Made: {self.date_made}, Top Speed: {self.top_speed}, Weight: {self.weight}, Engine: {self.engine}, Displacement: {self.displacement}, Price: {self.price}"

class HondaMotorcycle(Motorcycle):
    def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
        super().__init__(color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price)

    def start(self):
        if not self.is_running():
            self.engine = "on"
            return "Starting the motorcycle..."
        else:
            return "The motorcycle is already running."

    def stop(self):
        if self.is_running():
            self.engine = "off"
            return "Stopping the motorcycle..."
        else:
            return "The motorcycle is already stopped."

# Example usage
motorcycle = HondaMotorcycle("Black", "123", 10, 2, "Honda", "CBR1000", "2023", 200, 500, "off", "1000cc", "100,000")
print(motorcycle.start())
print(motorcycle.stop())
print(motorcycle.motorcycle_price())
print(motorcycle.motorcycle_fuel_left())
print(motorcycle.getDetails())
print(motorcycle.max_fuel_capacity(10))



'''
create a class called motorcycle with the following attributes: color, license_plate., fuel_liters, wheel_number, brand, model, date_made, top_speed, weight. engine, displacemnt. Add two smart methods, start and stop that will represent these two actions with motorcycles t.
Here's a class called `Motorcycle` with the given attributes and methods:
```python
class Motorcycle:
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement):
self.color = color
self.license_plate = license_plate
self.fuel_liters = fuel_liters
self.wheel_number = wheel_number
self.brand = brand
self.model = model
self.date_made = date_made
self.top_speed = top_speed
self.weight = weight
self.engine = engine
self.displacement = displacement

def start(self):
print("Starting the motorcycle...")

def stop(self):
print("Stopping the motorcycle...")
```
This class has two smart methods, `start` and `stop`, that are called when the motorcycle is started and stopped, respectively. The `start` method prints a message indicating that the motorcycle is being started, and the `stop` method prints a message indicating that the motorcycle is being stopped.

Here's an example usage of the `Motorcycle` class:
```python
motorcycle = Motorcycle("Black", "123", 10, 2, "Honda", "CBR1000", "2023", 200, 500, "inline 4")
print("Starting the motorcycle...")
motorcycle.start()
print("Stopping the motorcycle...")
motorcycle.stop()
```
In this example, a `Motorcycle` object is created with the given attributes and methods, and the `start` and `stop` methods are called to simulate the starting and stopping of the motorcycle.
Generate the code for this:
start() method, if the motor is stopped, it is indicated that the motor has started, if the motor is already running and an attempt is made to start it again, it is indicated that the motor was already running.
method stop(): if the motor is running, it is indicated that the motor has stopped, if the motor is already stopped, and an attempt is made to stop again, it is indicated that the motor was already stopped. Then Instance a motorcycle, the attributes fuel_liters and number_wheels must be the following values:
fuel liters = 10
number_wheels = 2
Here is the code for the start and stop methods of the `Motorcycle` class, with additional checks to indicate whether the motorcycle is already running or stopped:
```python
class Motorcycle:
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement):
self.color = color
self.license_plate = license_plate
self.fuel_liters = fuel_liters
self.wheel_number = wheel_number
self.brand = brand
self.model = model
self.date_made = date_made
self.top_speed = top_speed
self.weight = weight
self.engine = engine
self.displacement = displacement

def start(self):
if not self.is_running():
print("Starting the motorcycle...")
self.engine = "on"
else:
print("The motorcycle was already running.")

def stop(self):
if self.is_running():
print("Stopping the motorcycle...")
self.engine = "off"
else:
print("The motorcycle was already stopped.")

def is_running(self):
return self.engine == "on"

# Example usage
motorcycle = Motorcycle("Black", "123", 10, 2, "Honda", "CBR1000", "2023", 200, 500, "off", "1000cc")
print("Starting the motorcycle...")
motorcycle.start()
print("Stopping the motorcycle...")
motorcycle.stop()
```
In this code, the `start` method checks if the motorcycle is already running by checking if the `engine` attribute is not equal to the string `"off"`. If it is not running, it prints a message indicating that it is starting. If it is already running, it prints a message indicating that it was already running. Similarly, the `stop` method checks if the motorcycle is already stopped by checking if the `engine` attribute is equal to the string `"off"`. If it is not stopped, it prints a message indicating that it is stopping. If it is already stopped, it prints a message indicating that it was already stopped.
now add to this code the attribute price for the motorcycle, and make this an abstract class, then create a class called HondaMotorcycle which extends this class
Here is the updated code for the `Motorcycle` class with the `price` attribute as an abstract class, and the `HondaMotorcycle` class which extends it:
```python
from abc import ABC, abstractmethod

class Motorcycle(ABC):
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
self.color = color
self.license_plate = license_plate
self.fuel_liters = fuel_liters
self.wheel_number = wheel_number
self.brand = brand
self.model = model
self.date_made = date_made
self.top_speed = top_speed
self.weight = weight
self.engine = engine
self.displacement = displacement
self.price = price

@abstractmethod
def start(self):
pass

@abstractmethod
def stop(self):
pass

def is_running(self):
return self.engine == "on"

class HondaMotorcycle(Motorcycle):
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
super().__init__(color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price)

def start(self):
if not self.is_running():
print("Starting the motorcycle...")
self.engine = "on"
else:
print("The motorcycle was already running.")

def stop(self):
if self.is_running():
print("Stopping the motorcycle...")
self.engine = "off"
else:
print("The motorcycle was already stopped.")

# Example usage
motorcycle = HondaMotorcycle("Black", "123", 10, 2, "Honda", "CBR1000", "2023", 200, 500, "off", "1000cc", "100,000")
print("Starting the motorcycle...")
motorcycle.start()
print("Stopping the motorcycle...")
motorcycle.stop()
```
In this updated code, the `Motorcycle` class is now an abstract class, and the `HondaMotorcycle` class is a subclass that extends the `Motorcycle` class. The `HondaMotorcycle` class has all the same attributes and methods as the `Motorcycle` class, with the addition of the `price` attribute.
add a method to know the price of the motorcycle and a method to put its price and one for the amount of fuel_liters left
Here is the updated code for the `Motorcycle` class with the `price` and `fuel_left` methods:
```python
from abc import ABC, abstractmethod

class Motorcycle(ABC):
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
self.color = color
self.license_plate = license_plate
self.fuel_liters = fuel_liters
self.wheel_number = wheel_number
self.brand = brand
self.model = model
self.date_made = date_made
self.top_speed = top_speed
self.weight = weight
self.engine = engine
self.displacement = displacement
self.price = price

@abstractmethod
def start(self):
pass

@abstractmethod
def stop(self):
pass

def is_running(self):
return self.engine == "on"

def motorcycle_price(self):
return self.price

def motorcycle_fuel_left(self):
return self.fuel_liters

class HondaMotorcycle(Motorcycle):
def __init__(self, color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price):
super().__init__(color, license_plate, fuel_liters, wheel_number, brand, model, date_made, top_speed, weight, engine, displacement, price)

def start(self):
if not self.is_running():
self.engine = "on"
return "Starting the motorcycle..."
else:
return "The motorcycle is already running."

def stop(self):
if self.is_running():
self.engine = "off"
return "Stopping the motorcycle..."
else:
return "The motorcycle is already stopped."

# Example usage
motorcycle = HondaMotorcycle("Black", "123", 10, 2, "Honda", "CBR1000", "2023", 200, 500, "off", "1000cc", "100,000")
print(motorcycle.start())
print(motorcycle.stop())
print(motorcycle.motorcycle_price())
print(motorcycle.motorcycle_fuel_left())
```
In this updated code, the `motorcycle_price` and `motorcycle_fuel_left` methods have been added to the `Motorcycle` class . The `motorcycle_price` method returns the price of the motorcycle, and the `motorcycle_fuel_left` method returns the amount of fuel left in the motorcycle.
creates a method to determine the maximum liters of fuel that can be loaded to the motorcycle, in this case the maximum capacity is 20 liters. If a higher amount is indicated, a message should be sent by console and the user should be allowed to reload the fuel tank capacity as many times as necessary until a correct amount is entered. Once the correct amount is entered, the capacity of the motorcycle's fuel tank should be printed by console. It also adds an obtainDetails method to know all the details of the motorcycle.
'''