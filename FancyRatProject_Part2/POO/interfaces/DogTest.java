public class DogTest {
    public static void main(String[] args) {
        Dog dog = new Dog("PitBull", "brown", "Speedy");
        String name = dog.getName();
        dog.run();
        dog.walk();
        dog.eat(name);
        dog.drink_water(name);
        dog.sleep();
    }
}
