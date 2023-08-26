// Abstract class representing a person
public abstract class Person {
    protected String name;
    protected String job;

    // Constructor to initialize the name and job of the person
    protected Person(String name, String job) {
        this.name = name;
        this.job = job;
    }

    // Abstract method to be implemented by subclasses to make a sound
    public abstract void makeSound();

    // Getter and setter methods for name and job
    public String getName(){
        return this.name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getJob(){
        return this.job;
    }

    public void setJob(String job){
        this.job = job;
    }

}

// Concrete class representing a Lawyer, extending the Person class
public class Lawyer extends Person {
    public Lawyer(String name) {
        super(name, "Lawyer");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a lawyer.");
    }
}

// Concrete class representing a Programmer, extending the Person class
public class Programmer extends Person {
    public Programmer(String name) {
        super(name, "Programmer");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a programmer.");
    }
}

// Interface for a PersonFactory to create person instances
public interface PersonFactory {
    Person createPerson(String name);
}

// Concrete implementation of LawyerFactory, creating Lawyer instances
public class LawyerFactory implements PersonFactory {
    @Override
    public Person createPerson(String name) {
        return new Lawyer(name);
    }
}

// Concrete implementation of ProgrammerFactory, creating Programmer instances
public class ProgrammerFactory implements PersonFactory {
    @Override
    public Person createPerson(String name) {
        return new Programmer(name);
    }
}

// Main class to demonstrate the usage of factories and person instances
public class Main {
    public static void main(String[] args) {
        PersonFactory lawyerFactory = new LawyerFactory();
        Person lawyer = lawyerFactory.createPerson("John");
        lawyer.makeSound();

        PersonFactory programmerFactory = new ProgrammerFactory();
        Person programmer = programmerFactory.createPerson("Alice");
        programmer.makeSound();
    }
}
