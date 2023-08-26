// Concrete class representing a Nurse, extending the Person class
public class Nurse extends Professionals {
    public Nurse(String name) {
        super(name, "Nurse");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a nurse.");
    }
}
