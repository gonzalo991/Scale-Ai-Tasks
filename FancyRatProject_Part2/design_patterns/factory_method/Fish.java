// Concrete class representing a Fish, extending the Animal class
public class Fish extends Animal {
    public Fish(String name, int age, boolean isFemale){
        super(name, age, isFemale);
    }

    @Override
    public void makeSound(){
        System.out.println("glup glup!");
    }
}