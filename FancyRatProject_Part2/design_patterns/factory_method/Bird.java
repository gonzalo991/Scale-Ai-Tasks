// Concrete class representing a Bird, extending the Animal class
public class Bird extends Animal{
    public Bird(String name, int age, boolean isFemale){
        super(name, age, isFemale);
    }

    @Override
    public void makeSound(){
        System.out.println("pio pio!");
    }
}