public class Dog extends Pet {

    public String race;

    public Dog() {

    }

    public Dog(String name, int age, String breed, String color, String race) {
        super(name, color, breed, age);
        this.race = race;
    }

    public String getRace() {
        return race;
    }

    public void setRace(String race) {
        this.race = race;
    }

    public String eat(String action) {
        return "The dog is: " + action;
    }

    public String run(String action) {
        return "The dog is: " + action;
    }

    public String sleep(String action) {
        return "The dog is: " + action;
    }

    @Override
    public String toString() {
        return "Dog: { " + super.toString() + ", race: " + race + " }";
    }

    @Override
    public void eat() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'eat'");
    }

    @Override
    public void run() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'run'");
    }

    @Override
    public void sleep() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'sleep'");
    }
}