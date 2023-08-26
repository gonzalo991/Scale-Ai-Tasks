// Component interface
interface Component {
    void operation() throws Exception;
}

// Concrete component
class ConcreteComponent implements Component {
    @Override
    public void operation() throws Exception {
        System.out.println("ConcreteComponent operation");
    }
}

// Decorator interface
interface Decorator extends Component {
    Component getComponent();
}

// Concrete decorator
class MilkDecorator implements Decorator {
    private Component component;

    // Constructor to wrap a component
    public MilkDecorator(Component component) {
        this.component = component;
    }

    @Override
    public void operation() throws Exception {
        try {
            System.out.println("MilkDecorator operation");
            component.operation(); // Call operation of the wrapped component
        } catch (Exception e) {
            System.err.println("Operation failed in MilkDecorator: " + e.getMessage());
            throw e; // Re-throw the exception
        }
    }

    @Override
    public Component getComponent() {
        return component;
    }
}

// Concrete decorator
class SugarDecorator implements Decorator {
    private Component component;

    // Constructor to wrap a component
    public SugarDecorator(Component component) {
        this.component = component;
    }

    @Override
    public void operation() throws Exception {
        try {
            System.out.println("SugarDecorator operation");
            component.operation(); // Call operation of the wrapped component
        } catch (Exception e) {
            System.err.println("Operation failed in SugarDecorator: " + e.getMessage());
            throw e; // Re-throw the exception
        }
    }

    @Override
    public Component getComponent() {
        return component;
    }
}

