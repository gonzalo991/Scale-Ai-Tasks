# Memento class: Represents a saved state of a text editor.
class Memento:
    def __init__(self, state):
        self._state = state  # Initialize the Memento with the provided state.

    def get_state(self):
        return self._state  # Retrieve and return the stored state.

# Originator class: Represents the text editor.
class TextEditor:
    def __init__(self):
        self.content = []  # Initialize the content as an empty list.

    def set_content(self, content):
        self.content = content  # Set the content of the text editor.

    def get_content(self):
        return self.content  # Retrieve the content of the text editor.

    def create_memento(self):
        return Memento(self.content)  # Create a Memento with the current content.

    def restore_from_memento(self, memento):
        self.content = memento.get_state()  # Restore the content from a provided Memento.

# Caretaker class: Manages the creation and storage of Mementos.
class Caretaker:
    def __init__(self):
        self.mementos = []  # Initialize a list to store Mementos.

    def add_memento(self, memento):
        self.mementos.append(memento)  # Add a Memento to the list.

    def get_memento(self, index):
        return self.mementos[index]  # Retrieve the Memento at the specified index.

# Create a TextEditor instance.
text_editor = TextEditor()

# Set the content of the text editor.
text_editor.set_content(["Hello, World!"])

# Create a Memento containing the current content.
memento = text_editor.create_memento()

# Create a Caretaker object to store the Memento.
caretaker = Caretaker()

# Add the Memento to the Caretaker object.
caretaker.add_memento(memento)

# Retrieve the Memento from the Caretaker object.
retrieved_memento = caretaker.get_memento(0)

# Restore the content from the Memento.
text_editor.restore_from_memento(retrieved_memento)

print(f"Restored Content: {text_editor.get_content()}")