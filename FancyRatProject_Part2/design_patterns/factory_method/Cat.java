// Concrete class representing a Cat, extending the Animal class
public class Cat extends Animal {
    public Cat(String name, int age, boolean isFemale) {
        super(name, age, isFemale);
    }

    @Override
    public void makeSound() {
        System.out.println("Meow!");
    }
}