from abc import ABC, abstractmethod

# Step 1: Define the abstract base class (Component)
class Box(ABC):

    @abstractmethod
    def calculate_weight(self):
        pass

    @abstractmethod
    def amount_of_items(self):
        pass

    @abstractmethod
    def print_content(self):
        pass

# Step 2: Create concrete classes that implement the Component interface
class CandyBox(Box):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def calculate_weight(self):
        return self.weight

    def amount_of_items(self):
        return 1

    def print_content(self):
        print(f"Candy: {self.name}")

# Step 3: Create the composite class
class BigCandyBox(Box):
    def __init__(self, name):
        self.name = name
        self.boxes = []

    def calculate_weight(self):
        total_weight = sum(box.calculate_weight() for box in self.boxes)
        return total_weight

    def amount_of_items(self):
        return sum(box.amount_of_items() for box in self.boxes)

    def print_content(self):
        print(f"Big Box: {self.name}")
        for box in self.boxes:
            box.print_content()

    def add_box(self, box):
        self.boxes.append(box)

# Step 4: Create a new class for the trailer
class Trailer(Box):
    def __init__(self, name):
        self.name = name
        self.boxes = []

    def calculate_weight(self):
        total_weight = sum(box.calculate_weight() for box in self.boxes)
        return total_weight

    def amount_of_items(self):
        return sum(box.amount_of_items() for box in self.boxes)

    def print_content(self):
        print(f"Trailer: {self.name}")
        for box in self.boxes:
            box.print_content()

    def add_box(self, box):
        self.boxes.append(box)

# Usage
candy1 = CandyBox("Chocolate", 0.2)
candy2 = CandyBox("Lollipop", 0.1)

big_box = BigCandyBox("Large Box")
big_box.add_box(candy1)
big_box.add_box(candy2)

small_box = BigCandyBox("Small Box")
small_box.add_box(candy2)

big_box.add_box(small_box)

trailer = Trailer("Cargo Trailer")
trailer.add_box(big_box)
trailer.add_box(candy2)

print("Total Weight:", trailer.calculate_weight())
print("Total Items:", trailer.amount_of_items())
trailer.print_content()
