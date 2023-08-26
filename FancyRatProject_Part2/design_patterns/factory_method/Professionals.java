// Abstract class representing a person
public abstract class Professionals {
    protected String name;
    protected String job;

    // Constructor to initialize the name and job of the person
    protected Professionals(String name, String job) {
        this.name = name;
        this.job = job;
    }

    // Abstract method to be implemented by subclasses to make a sound
    public abstract void makeSound();

    // Getter and setter methods for name and job
    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getJob() {
        return this.job;
    }

    public void setJob(String job) {
        this.job = job;
    }
}









