# Memento class: Represents a saved state of an object.
class Memento:
    def __init__(self, state):
        self._state = state # Initialize the Memento with the provided state.

    def get_state(self):
        return self._state # Retrieve and return the stored state.

# Originator class: Represents an object whose state can be saved and restored.
class Originator:
    def __init__(self, state):
        self._state = state # Initialize the Originator with an initial state.

    def create_memento(self):
        return Memento(self._state) # Create a Memento containing the current state.

    def restore_from_memento(self, memento):
        self._state = memento.get_state() # Restore the state from a provided Memento.

    def set_state(self, state):
        self._state = state # Set the current state of the Originator.

# Caretaker class: Manages the creation and storage of Mementos.
class Caretaker:
    def __init__(self):
        self.mementos = []  # Initialize a list to store Mementos.

    def add_memento(self, memento):
        self.mementos.append(memento)  # Add a Memento to the list.

    def get_memento(self, index):
        return self.mementos[index]  # Retrieve the Memento at the specified index.
    
# Create a Memento containing the current state.
memento = originator.create_memento()

# Create a Caretaker object to store the Memento.
caretaker = Caretaker()

# Add the Memento to the Caretaker object.
caretaker.add_memento(memento)

# Retrieve the Memento from the Caretaker object.
retrieved_memento = caretaker.get_memento(0)

# Restore the state from the Memento.
originator.restore_from_memento(retrieved_memento)