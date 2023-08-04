public abstract class Pet {
    protected String name;
    protected String breed;
    protected String color;
    protected int age;

    public Pet() {
    }

    public Pet(String name, String breed, String color, int age) {
        this.name = name;
        this.breed = breed;
        this.color = color;
        this.age = age;
    }

    public abstract void eat();
    public abstract void run();
    public abstract void sleep();

    public String getName() {
        return this.name;
    }

    public String getBreed() {
        return this.breed;
    }

    public String getColor() {
        return this.color;
    }

    public int getAge() {
    return this.age;
    }
}