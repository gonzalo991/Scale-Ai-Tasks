// Main class to demonstrate the usage of factories and person instances
public class ProfessionalsTest {
    public static void main(String[] args) {
        PersonFactory lawyerFactory = new LawyerFactory();
        Person lawyer = lawyerFactory.createPerson("Jorge");
        lawyer.makeSound();

        PersonFactory programmerFactory = new ProgrammerFactory();
        Person programmer = programmerFactory.createPerson("Lorena");
        programmer.makeSound();

        PersonFactory nurseFactory = new NurseFactory();
        Person nurse = nurseFactory.createPerson("Mario");
        nurse.makeSound();

        PersonFactory teacherFactory = new TeacherFactory();
        Person teacher = teacherFactory.createPerson("Carla");
        teacher.makeSound();
    }
}