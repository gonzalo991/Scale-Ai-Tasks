class Vehicle:
    def __init__(self, vehicle_type, color, motor, isFull, fuel_type, price):
        self.vehicle_type = vehicle_type
        self.color = color
        self.motor = motor
        self.isFull = isFull
        self.fuel_type = fuel_type
        self.price = price
        self.is_turned_on = False
        self.speed = 0

    def turn_on(self):
        if not self.is_turned_on:
            print(f"Turning on the {self.vehicle_type}")
            self.is_turned_on = True
        else:
            print(f"The {self.vehicle_type} is already on.")

    def turn_off(self):
        if self.is_turned_on:
            print(f"Turning off the {self.vehicle_type}")
            self.is_turned_on = False
            self.speed = 0
        else:
            print(f"The {self.vehicle_type} is already off.")

    def accelerate(self, speed):
        if self.is_turned_on:
            self.speed += speed
            print(f"The {self.vehicle_type} is accelerating to {self.speed} km/h.")
        else:
            print(f"The {self.vehicle_type} is not turned on.")

    def activate_break(self, speed):
        if self.is_turned_on:
            self.speed -= speed
            if self.speed < 0:
                self.speed = 0
            print(f"The {self.vehicle_type} is decelerating to {self.speed} km/h.")
        else:
            print(f"The {self.vehicle_type} is not turned on.")

    def drive(self, acceleration, deceleration):
        if not self.is_turned_on:
            print(f"Can't drive. The {self.vehicle_type} is not turned on.")
            return
        
        print(f"Driving the {self.vehicle_type}...")
        self.accelerate(acceleration)
        self.activate_break(deceleration)
        print(f"Arrived at destination. Stopping the {self.vehicle_type}.")
        self.turn_off()

    def __str__(self):
        return f"Vehicle Type: {self.vehicle_type}\nColor: {self.color}\nMotor: {self.motor}\nIs Full: {self.isFull}\nFuel Type: {self.fuel_type}\nPrice: {self.price}\nIs Turned On: {self.is_turned_on}\nSpeed: {self.speed}"

# Create instances of vehicles in the dealership
vehicles = [
    Vehicle("Car", "Red", "V8", True, "Gasoline", 35000),
    Vehicle("Motorcycle", "Black", "Inline 4", True, "Gasoline", 12000),
    Vehicle("Truck", "Blue", "V8", True, "Diesel", 60000)
]

# Display vehicle details to customers
print("Welcome to Our Dealership!")
for idx, vehicle in enumerate(vehicles, start=1):
    print(f"\nVehicle {idx} Details:")
    print(vehicle)

# Allow customers to test drive vehicles
try:
    selected_vehicle_idx = int(input("\nEnter the number of the vehicle you want to test drive: ")) - 1
    if 0 <= selected_vehicle_idx < len(vehicles):
        selected_vehicle = vehicles[selected_vehicle_idx]
        print(f"\nYou've selected the {selected_vehicle.vehicle_type} for a test drive.")
        selected_vehicle.turn_on()
        selected_vehicle.accelerate(30)
        selected_vehicle.activate_brake(10)
        selected_vehicle.turn_off()
    else:
        print("Invalid vehicle number. Please select a valid vehicle.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("\nThank you for visiting our dealership!")