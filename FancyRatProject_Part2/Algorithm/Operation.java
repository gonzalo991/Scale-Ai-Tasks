// This is a Java class named 'Operation'.
public class Operation {
    // Inside the class, there are three private integer variables: 'a', 'b', and
    // 'c'.
    private int a;
    private int b;
    private int c;

    // The class has two constructors:
    // 1. A default constructor with no arguments, which does nothing.
    public Operation() {
    }

    // 2. A parameterized constructor with three integer arguments ('a', 'b', and
    // 'c').
    // It initializes the 'a', 'b', and 'c' variables with the provided values.
    public Operation(int a, int b, int c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    // There are getter and setter methods for each variable:
    // - Getter method 'getA()' returns the value of 'a'.
    public int getA() {
        return a;
    }

    // - Setter method 'setA(int a)' sets the value of 'a' to the provided argument.
    public void setA(int a) {
        this.a = a;
    }

    // - Getter method 'getB()' returns the value of 'b'.
    public int getB() {
        return b;
    }

    // - Setter method 'setB(int b)' sets the value of 'b' to the provided argument.
    public void setB(int b) {
        this.b = b;
    }

    // - Getter method 'getC()' returns the value of 'c'.
    public int getC() {
        return c;
    }

    // - Setter method 'setC(int c)' sets the value of 'c' to the provided argument.
    public void setC(int c) {
        this.c = c;
    }

    // Method that creates a new Operation object and initializes its attributes
    // with the provided numbers.
    public static Operation createOperation(int a, int b, int c) {
        Operation operation = new Operation(a, b, c);
        return operation;
    }

    // Method that returns the sum of the three attributes 'a', 'b', and 'c'.
    public int sum() {
        int sum = a + b + c;
        return sum;
    }

    // Method to subtract 'b' from 'a' and set the result to 'c'
    public void subtractBFromA() {
        try {
            this.c = this.a - this.b;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to subtract 'c' from 'b' and set the result to 'a'
    public void subtractCFromB() {
        try {
            this.a = this.b - this.c;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to subtract 'c' from 'a' and set the result to 'b'
    public void subtractCFromA() {
        try {
            this.b = this.a - this.c;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

     // Method to subtract 'a' from 'c' and set the result to 'b'
    public void subtractAFromC() {
        try {
            this.b = this.c - this.a;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to subtract 'a' from 'b' and set the result to 'c'
    public void subtractAFromB() {
        try {
            this.c = this.b - this.a;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    // Method to subtract 'b' from 'c' and set the result to 'a'
    public void subtractBFromC() {
        try {
            this.a = this.c - this.b;
        } catch (ArithmeticException e) {
            System.err.println("Error: ArithmeticException - Division by zero.");
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Operation operation = new Operation();
        operation.setA(10);
        operation.setB(5);
        operation.setC(2);

        operation.subtractBFromA();
        System.out.println("Result of subtracting B from A: " + operation.getC()); // Output: Result of subtracting B from A: 5

        operation.subtractCFromB();
        System.out.println("Result of subtracting C from B: " + operation.getA()); // Output: Result of subtracting C from B: 0 

        operation.subtractCFromA();
        System.out.println("Result of subtracting C from A: " + operation.getB()); // Output: Result of subtracting C from A: -5
    }
}