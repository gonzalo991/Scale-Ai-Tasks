public class Dog extends Pet{
    
    public String race;
    
    public Dog(){

    }

    public Dog(String name, int age, String breed, String color, String race){
        super(name, age, breed, color);
        this.race = race;
    }

    public String getRace() {
            return race;
    }

    public void setRace(String race) {
        this.race = race;
    }

    public String eat(String action) {
        return "The dog is: "+ action;
    }

    public String run(String action) {
        return "The dog is: "+ action;
    }

    public String sleep(String action) {
        return "The dog is: "+ action;
    }


    @Override
    public String toString() {
        return "Dog: { " + super.toString() + ", race: " + race + " }";
    }
}