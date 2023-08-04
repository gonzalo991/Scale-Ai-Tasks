public class Cat extends Pet {

    public Cat() {

    }

    public Cat(String name, String breed, String color) {
        super(name, breed, color, 0); // The age is set to 0 for cats; you can set the actual age as per your requirement.
    }

    @Override
    public void eat() {
        // Implement the eating behavior of the cat
        System.out.println("The cat is eating.");
    }

    @Override
    public void run() {
        // Implement the running behavior of the cat
        System.out.println("The cat is running.");
    }

    @Override
    public void sleep() {
        // Implement the sleeping behavior of the cat
        System.out.println("The cat is sleeping.");
    }

    @Override
    public String toString() {
        return "Cat: { " + super.toString() + " }"; 
    }
}
