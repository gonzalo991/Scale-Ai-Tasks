// Concrete implementation of DogFactory, creating Dog instances
public class DogFactory implements AnimalFactory {
    @Override
    public Animal createAnimal(String name, int age, boolean isFemale) {
        return new Dog(name, age, isFemale);
    }
}
