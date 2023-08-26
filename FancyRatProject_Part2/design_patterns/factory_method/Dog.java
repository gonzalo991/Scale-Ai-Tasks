// Concrete class representing a Dog, extending the Animal class
public class Dog extends Animal {
    public Dog(String name, int age, boolean isFemale) {
        super(name, age, isFemale);
    }

    @Override
    public void makeSound() {
        System.out.println("Woof!");
    }
}