// Abstract class representing an animal
public abstract class Animal {
    protected String name;
    protected int age;
    protected boolean isFemale;

    // Constructor to initialize the name, age, and gender of the animal
    protected Animal(String name, int age, boolean isFemale) {
        this.name = name;
        this.age = age;
        this.isFemale = isFemale;
    }

    // Abstract method to be implemented by subclasses to make a sound
    public abstract void makeSound();

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public boolean isFemale() {
        return this.isFemale;
    }

    public void setFemale(boolean female) {
        this.isFemale = female;
    }
}