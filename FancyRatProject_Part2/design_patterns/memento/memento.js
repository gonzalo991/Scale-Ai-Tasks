class Memento {
    constructor(value) {
        this.value = value;
    }

    getState() {
        console.log("State:", this.value);
        return this.value;
    }
}

class Originator {
    constructor() {
        this.state = '';
    }

    createMemento() {
        return new Memento(this.state);
    }

    restoreFromMemento(memento) {
        this.setState(memento.getState());
    }

    getState() {
        console.log("State:", this.state);
        return this.state;
    }

    setState(state) {
        console.log("Setting state:", state);
        this.state = state;
    }
}


class Caretaker {
    constructor() {
        this.mementos = [];
    }

    addMemento(memento) {
        this.mementos.push(memento);
    }

    getMemento(index) {
        return this.mementos[index];
    }
}