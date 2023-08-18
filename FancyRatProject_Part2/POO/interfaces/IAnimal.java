public interface IAnimal{
    void run();

    void walk();

    default void eat(String animal){
        System.out.println("The animal "+animal+" is eating...");
    };

    default void drink_water(String animal){
        System.out.println("The animal "+animal+" is drinking water...");
    }

    void sleep();
}