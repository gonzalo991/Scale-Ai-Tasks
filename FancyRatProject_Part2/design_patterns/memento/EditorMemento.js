// Memento class: Represents a specific state of the text editor.
class EditorMemento {
    constructor(content, cursorPosition) {
        this.content = content;
        this.cursorPosition = cursorPosition;
    }

    // Method to retrieve the content and cursor position of the memento.
    getState() {
        console.log("Content:", this.content);
        console.log("Cursor Position:", this.cursorPosition);
        return { content: this.content, cursorPosition: this.cursorPosition };
    }
}

// Text editor class: Represents a text editor and its state.
class Editor {
    constructor() {
        this.content = ""; // Content of the text editor
        this.cursorPosition = 0; // Cursor position within the content
    }

    // Method to create a memento of the current state of the text editor.
    createMemento() {
        return new EditorMemento(this.content, this.cursorPosition);
    }

    // Method to restore the state of the text editor from a memento.
    restoreFromMemento(memento) {
        if (memento) {
            const { content, cursorPosition } = memento.getState();
            this.content = content;
            this.cursorPosition = cursorPosition;
        } else {
            console.log("Invalid memento provided.");
        }
    }

    // Method to insert text at the current cursor position.
    insertText(text) {
        this.content = this.content.slice(0, this.cursorPosition) + text + this.content.slice(this.cursorPosition);
        this.cursorPosition += text.length;
    }

    // Method to delete text at the current cursor position.
    deleteText(text) {
        this.content = this.content.slice(0, this.cursorPosition) + this.content.slice(this.cursorPosition + text.length);
        this.cursorPosition -= text.length;
    }

    // Method to display the current content of the text editor.
    displayContent() {
        console.log("Content:", this.content);
    }
}

// Caretaker class: Manages the text editor's mementos.
class EditorCaretaker {
    constructor() {
        this.mementos = []; // Mementos of the text editor
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

// Create instances of the text editor and the caretaker
const editor = new Editor();
const caretaker = new EditorCaretaker();

// The user types in the text editor and saves the state
editor.insertText("Hello, world!");
caretaker.addMemento(editor.createMemento());

// The user types in the text editor again and saves the state
editor.insertText("This is a test.");
caretaker.addMemento(editor.createMemento());

// The user wants to restore a previous state
editor.restoreFromMemento(caretaker.getMemento(1));

// Display the current content of the text editor
editor.displayContent();
console.log("Restored content!");