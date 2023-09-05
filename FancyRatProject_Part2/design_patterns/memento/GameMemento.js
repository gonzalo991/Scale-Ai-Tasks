// Memento Class: Captures the game state.
class GameMemento {
    constructor(level, score) {
        this.level = level;
        this.score = score;
    }

    getLevel() {
        return this.level;
    }

    getScore() {
        return this.score;
    }
}

// Game Class: Represents the game and its state.
class Game {
    constructor() {
        this.level = 1; // Current game level
        this.score = 0; // Player's score
    }

    // Method to create a memento of the current game state
    createMemento() {
        return new GameMemento(this.level, this.score);
    }

    // Method to restore the game state from a memento
    restoreFromMemento(memento) {
        this.level = memento.getLevel();
        this.score = memento.getScore();
    }

    // Method to play and update the game state
    play() {
        this.level++;
        this.score += 100;
        console.log(`Level ${this.level} completed. Total score: ${this.score}`);
    }
}

// Caretaker Class: Manages the game's mementos.
class GameCaretaker {
    constructor() {
        this.mementos = [];
    }

    // Add a memento to the list
    addMemento(memento) {
        this.mementos.push(memento);
    }

    // Get a memento from the list by index
    getMemento(index) {
        return this.mementos[index];
    }
}

// Create instances of the game and the caretaker
const game = new Game();
const caretaker = new GameCaretaker();

// The player progresses in the game and saves the progress
game.play();
caretaker.addMemento(game.createMemento());

game.play();
caretaker.addMemento(game.createMemento());

game.play();
caretaker.addMemento(game.createMemento());

// The player decides to load a previous game state
game.restoreFromMemento(caretaker.getMemento(1));

console.log("Current level:", game.level); // Should print 2
console.log("Current score:", game.score); // Should print 200
