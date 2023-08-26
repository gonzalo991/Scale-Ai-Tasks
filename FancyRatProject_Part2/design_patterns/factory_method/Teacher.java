// Concrete class representing a Teacher, extending the Person class
public class Teacher extends Professionals {
    public Teacher(String name) {
        super(name, "Teacher");
    }

    @Override
    public void makeSound() {
        System.out.println("Hello, my name is " + this.getName() + " and I am a teacher.");
    }
}
