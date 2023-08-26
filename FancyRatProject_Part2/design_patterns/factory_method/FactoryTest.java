// Main class to demonstrate the usage of factories and animal instances
public class FactoryTest {
    public static void main(String[] args) {
        AnimalFactory dogFactory = new DogFactory();
        Animal dog = dogFactory.createAnimal("Dog", 3, true);
        dog.makeSound();

        AnimalFactory catFactory = new CatFactory();
        Animal cat = catFactory.createAnimal("Cat", 2, false);
        cat.makeSound();
    }
}