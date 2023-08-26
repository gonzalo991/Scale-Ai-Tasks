import java.util.Arrays;
import java.util.List;

public class Client {
    public static void main(String[] args) {
        // Create a list of components
        List<Component> components = Arrays.asList(
            new ConcreteComponent(),
            new MilkDecorator(new ConcreteComponent()),
            new SugarDecorator(new MilkDecorator(new ConcreteComponent()))
        );

        // Iterate through components and perform operations with error handling
        for (Component component : components) {
            try {
                component.operation();
            } catch (Exception e) {
                System.err.println("Operation failed: " + e.getMessage());
            }
        }
    }
}
