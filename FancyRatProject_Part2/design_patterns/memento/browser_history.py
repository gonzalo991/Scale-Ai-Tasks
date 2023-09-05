# Memento class: Represents a saved state of a browser history.
class Memento:
    def __init__(self, state):
        self._state = state # Initialize the Memento with the provided state.

def get_state(self):
    return self._state # Retrieve and return the stored state.

# Originator class: Represents the browser history.
class BrowserHistory:
    def __init__(self):
        self.history = [] # Initialize the history as an empty list.

    def add_history(self, url):
        self.history.append(url) # Add a new history item.

    def remove_history(self, index):
        self.history.pop(index) # Remove the history item at the specified index.

    def create_memento(self):
        return Memento(self.history) # Create a Memento with the current history.

    def restore_from_memento(self, memento):
        self.history = memento.get_state() # Restore the history from a provided Memento.

    def set_state(self, state):
        self.history = state # Set the current history.

# Caretaker class: Manages the creation and storage of Mementos.
class Caretaker:
    def __init__(self):
        self.mementos = [] # Initialize a list to store Mementos.

    def add_memento(self, memento):
        self.mementos.append(memento) # Add a Memento to the list.

    def get_memento(self, index):
        return self.mementos[index] # Retrieve the Memento at the specified index.

# Create a BrowserHistory instance.
browser_history = BrowserHistory()

# Add some history items.
browser_history.add_history("https://www.example.com/")
browser_history.add_history("https://www.example.org/")
browser_history.add_history("https://www.example.net/")

# Create a Memento containing the current history.
memento = browser_history.create_memento()

# Create a Caretaker object to store the Memento.
caretaker = Caretaker()

# Add the Memento to the Caretaker object.
caretaker.add_memento(memento)

# Retrieve the Memento from the Caretaker object.
retrieved_memento = caretaker.get_memento(0)

# Restore the history from the Memento.
browser_history.restore_from_memento(retrieved_memento)

print(f"Restored History: {browser_history.history}")