# Define the Player class
class Player:
    def __init__(self, name):
        # Constructor initializes player's name and an empty list to store scores
        self._name = name
        self._scores = []

    def __str__(self):
        # Returns a formatted string representation of the player's name and number of scores
        return f"{self._name} has {len(self._scores)} scores."

    def add_score(self, score):
        # Method to add a score to the player's list of scores
        try:
            self._scores.append(score)
        except:
            print(f"Error adding score. Score must be a GameScore object.")

    def show_scores(self):
        # Method to display all the player's scores with associated game IDs
        try:
            for score in self._scores:
                print(f"Game {score._game_id}: {score._score}")
        except:
            print("Error displaying scores. Scores must be GameScore objects.")

# Define the GameScore class
class GameScore:
    def __init__(self, game_id, score):
        # Constructor initializes game ID and score
        self._game_id = game_id
        self._score = score

    def __str__(self):
        # Returns a formatted string representation of the game score
        return f"Game {self._game_id}: Score {self._score}"

# Usage example
# Create player objects
player1 = Player('Gonzalo')
player2 = Player('Joaquín')

# Create game scores
game_score1 = GameScore(1, 150)
game_score2 = GameScore(2, 250)

# Add game scores to players
player1.add_score(game_score1)
player2.add_score(game_score2)

# Display scores for each player
print("Scores for player 1:")
player1.show_scores()

print("Scores for player 2:")
player2.show_scores()