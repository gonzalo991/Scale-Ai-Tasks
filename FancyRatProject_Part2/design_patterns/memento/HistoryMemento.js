// Memento class: Represents a specific state of the browser history.
class HistoryMemento {
    constructor(url, title, time) {
        this.url = url;
        this.title = title;
        this.time = time;
    }

    // Method to retrieve the URL, title, and time of the memento.
    getState() {
        console.log("URL:", this.url);
        console.log("Title:", this.title);
        console.log("Time:", this.time);
        return { url: this.url, title: this.title, time: this.time };
    }
}

// Browser class: Represents the browser and its history.
class Browser {
    constructor() {
        this.history = []; // History of the browser
    }

    // Method to create a memento of the current history state
    createMemento() {
        if (this.history.length > 0) {
            const current = this.history[this.history.length - 1];
            return new HistoryMemento(current.url, current.title, current.time);
        } else {
            console.log("No history to create a memento from.");
            return null;
        }
    }

    // Method to restore the history state from a memento
    restoreFromMemento(memento) {
        if (memento) {
            const { url, title, time } = memento.getState();
            this.history.push({ url, title, time });
        } else {
            console.log("Invalid memento provided.");
        }
    }

    // Method to navigate to a web page and update the history
    navigate(url, title) {
        const time = new Date().toLocaleString();
        this.history.push({ url, title, time });
        console.log(`Navigated to: ${title} (${url})`);
    }

    // Method to display the current history state
    displayHistory() {
        console.log("Current history:");
        for (let i = 0; i < this.history.length; i++) {
            const entry = this.history[i];
            console.log(`- ${entry.title} (${entry.url}) - Visited at ${entry.time}`);
        }
    }
}

// Caretaker class: Manages the browser's mementos.
class BrowserCaretaker {
    constructor() {
        this.mementos = []; // Mementos of the browser history
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

// Create instances of the browser and the caretaker
const browser = new Browser();
const caretaker = new BrowserCaretaker();

// The user navigates through the browser and saves the history
browser.navigate("https://example.com", "Example Website");
browser.navigate("https://example.net", "ExampleNet Website");
browser.navigate("https://example.org", "ExampleOrg Website");

const memento1 = browser.createMemento();
caretaker.addMemento(memento1);

// The user navigates further
browser.navigate("https://newwebsite.com", "New Website");

const memento2 = browser.createMemento();
caretaker.addMemento(memento2);

// The user restores a previous history state
browser.restoreFromMemento(caretaker.getMemento(1));

// Display the current history
browser.displayHistory();
console.log("Restored history state!");
