// Concrete implementation of FishFactory, creating Cat instances
public class FishFactory implements AnimalFactory{
    @Override
    public Animal createAnimal(String name, int age, boolean isFemale){
        return new Fish(name, age, isFemale);
    }
}
