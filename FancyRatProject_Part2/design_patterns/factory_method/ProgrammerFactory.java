// Concrete implementation of ProgrammerFactory, creating Programmer instances
public class ProgrammerFactory implements ProfessionalsFactory {
    @Override
    public Professionals createPerson(String name) {
        return new Programmer(name);
    }
}