// Concrete implementation of TeacherFactory, creating Teacher instances
public class TeacherFactory implements ProfessionalsFactory {
    @Override
    public Professionals createPerson(String name) {
        return new Teacher(name);
    }
}
