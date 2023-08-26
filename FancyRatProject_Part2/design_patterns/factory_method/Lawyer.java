// Concrete class representing a Lawyer, extending the Person class
public class Lawyer extends Professionals {
    public Lawyer(String name) {
        super(name, "Lawyer");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a lawyer.");
    }
}