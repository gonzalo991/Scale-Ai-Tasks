class PersonFactory {
    createPerson(name, surname, age, occupation) {
        try {
            if (name && surname && age && !isNaN(age)) {
                if (this.isDuplicate(name, surname)) {
                    throw new Error('Person with the same name and surname already exists.');
                }
                const person = new Person(name, surname, age, occupation);
                this.persons.push(person);
                return person;
            } else {
                throw new Error('Invalid arguments. Name, surname, and age are required.');
            }
        } catch (error) {
            console.error(error.message);
            return new Person('Unknown', 'Unknown', 0, 'Unknown');
        }
    }

    isDuplicate(name, surname) {
        return this.persons.some(person => person.name === name && person.surname === surname);
    }
}

class Person {
    constructor(name, surname, age, occupation) {
        this.name = name;
        this.surname = surname;
        this.age = age;
        this.occupation = occupation;
        this.factory = null; // Initialize the factory property
    }

    setFactory(factory) {
        this.factory = factory;
    }

    describe() {
        return `${this.name} ${this.surname}, ${this.age} years old ${this.occupation}`;
    }
}

class EmployeeFactory extends PersonFactory {
    createPerson(name, surname, age) {
        return new Employee(name, surname, age);
    }
}

class Employee extends Person {
    constructor(name, surname, age) {
        super(name, surname, age, "Employee");
    }
}

class StudentFactory extends PersonFactory {
    createPerson(name, surname, age) {
        return new Student(name, surname, age);
    }
}

class Student extends Person {
    constructor(name, surname, age) {
        super(name, surname, age, "Student");
    }
}

// Usage example
const employeeFactory = new EmployeeFactory();
const studentFactory = new StudentFactory();

const jane = employeeFactory.createPerson('Jane', 'Smith', 30);
const john = studentFactory.createPerson('John', 'Doe', 22);

console.log(jane.describe());
console.log(john.describe());

// Create a person with invalid arguments
console.log('Creating a person with invalid arguments...');
const invalidPerson = studentFactory.createPerson('Jane', 'Smith', '22');
console.log(invalidPerson.describe());

// Trying to create a person with a duplicate name and surname
const duplicatePerson = studentFactory.createPerson('Jane', 'Smith', 25);

console.log(duplicatePerson.describe());