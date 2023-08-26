// Concrete implementation of BirdFactory, creating Cat instances
public class BirdFactory implements AnimalFactory {
    @Override
    public Animal createAnimal(String name, int age, boolean isFemale){
        return new Bird(name, age, isFemale);
    }
}