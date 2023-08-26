// Concrete class representing a Programmer, extending the Person class
public class Programmer extends Professionals {
    public Programmer(String name) {
        super(name, "Programmer");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a programmer.");
    }
}