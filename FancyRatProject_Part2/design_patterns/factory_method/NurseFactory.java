// Concrete implementation of NurseFactory, creating Nurse instances
public class NurseFactory implements ProfessionalsFactory {
    @Override
    public Professionals createPerson(String name) {
        return new Nurse(name);
    }
}
