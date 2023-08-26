// Concrete implementation of LawyerFactory, creating Lawyer instances
public class LawyerFactory implements ProfessionalsFactory { 
    @Override
    public Professionals createPerson(String name) {
        return new Lawyer(name);
    }
}