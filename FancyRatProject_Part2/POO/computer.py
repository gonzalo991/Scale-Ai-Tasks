from abc import ABC, abstractmethod

# Define an abstract base class for computer components
class ComputerComponent(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def describe(self):
        pass

# Define concrete classes for specific computer components
class Monitor(ComputerComponent):
    def __init__(self, make, model, inches):
        super().__init__(make, model)
        self.inches = inches

    def describe(self):
        return f"{self.make} {self.model} Monitor ({self.inches} inches)"

class Keyboard(ComputerComponent):
    def __init__(self, make, model, distribution):
        super().__init__(make, model)
        self.distribution = distribution

    def describe(self):
        return f"{self.make} {self.model} Keyboard ({self.distribution} layout)"

class Mouse(ComputerComponent):
    def __init__(self, make, model, is_gamer, buttons_number):
        super().__init__(make, model)
        self.is_gamer = is_gamer
        self.buttons_number = buttons_number

    def describe(self):
        return f"{self.make} {self.model} Mouse (Gamer: {self.is_gamer}, Buttons: {self.buttons_number})"

class CPU(ComputerComponent):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def describe(self):
        return f"{self.make} {self.model} CPU ({self.year})"

# Define the Computer class using the abstract base class
class Computer:
    def __init__(self, make, model, monitor, keyboard, mouse, cpu):
        self.make = make
        self.model = model
        self.monitor = monitor
        self.keyboard = keyboard
        self.mouse = mouse
        self.cpu = cpu

    def run(self):
        print("Starting the computer...")
        print(f"Computer components:")
        print(f"Monitor: {self.monitor.describe()}")
        print(f"Keyboard: {self.keyboard.describe()}")
        print(f"Mouse: {self.mouse.describe()}")
        print(f"CPU: {self.cpu.describe()}")
        print("Booting CPU...")
        print("Loading operating system...")
        print("Starting up...")

    def shutdown(self):
        print("Shutting down...")
        print("Powering off...")

# Example usage
monitor = Monitor("ASUS", "Gaming", 24)
keyboard = Keyboard("Logitech", "K123", "QWERTY")
mouse = Mouse("Razer", "M456", True, 6)
cpu = CPU("Intel", "i7", 2023)
computer = Computer("HP", "EliteBook", monitor, keyboard, mouse, cpu)

# Run and shut down the computer
computer.run()
computer.shutdown()