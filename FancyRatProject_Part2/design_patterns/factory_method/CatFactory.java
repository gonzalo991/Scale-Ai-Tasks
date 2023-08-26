// Concrete implementation of CatFactory, creating Cat instances
public class CatFactory implements AnimalFactory {
    @Override
    public Animal createAnimal(String name, int age, boolean isFemale) {
        return new Cat(name, age, isFemale);
    }
}

