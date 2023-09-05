# Memento class: Represents a saved state of a game progress.
class Memento:
    def __init__(self, state):
        self._state = state  # Initialize the Memento with the provided state.

    def get_state(self):
        return self._state  # Retrieve and return the stored state.

# Originator class: Represents the game progress.
class GameProgress:
    def __init__(self):
        self.level = 1  # Initialize the level.
        self.score = 0  # Initialize the score.

    def update_score(self, score):
        self.score += score  # Update the score.

    def update_level(self, level):
        self.level += 1  # Update the level.

    def create_memento(self):
        return Memento(f"Level: {self.level}, Score: {self.score}")  # Create a Memento with the current progress.

    def restore_from_memento(self, memento):
        state = memento.get_state().split(', ')  # Split the state into level and score.
        self.level = int(state[0].split(': ')[1])  # Extract and convert the level.
        self.score = int(state[1].split(': ')[1])  # Extract and convert the score.

    def set_state(self, state):
        self.level = int(state.split(', ')[0].split(': ')[1])  # Extract and convert the level.
        self.score = int(state.split(', ')[1].split(': ')[1])  # Extract and convert the score.

# Caretaker class: Manages the creation and storage of Mementos.
class Caretaker:
    def __init__(self):
        self.mementos = []  # Initialize a list to store Mementos.

    def add_memento(self, memento):
        self.mementos.append(memento)  # Add a Memento to the list.

    def get_memento(self, index):
        return self.mementos[index]  # Retrieve the Memento at the specified index.

# Create a GameProgress instance.
game_progress = GameProgress()

# Update the progress of the game.
game_progress.update_score(100)
game_progress.update_level(2)

# Create a Memento containing the current progress.
memento = game_progress.create_memento()

# Create a Caretaker object to store the Memento.
caretaker = Caretaker()

# Add the Memento to the Caretaker object.
caretaker.add_memento(memento)

# Retrieve the Memento from the Caretaker object.
retrieved_memento = caretaker.get_memento(0)

# Restore the progress from the Memento.
game_progress.restore_from_memento(retrieved_memento)

print(f"Restored Progress: Level {game_progress.level}, Score {game_progress.score}")
