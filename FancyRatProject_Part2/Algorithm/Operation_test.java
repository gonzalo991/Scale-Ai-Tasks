public class Operation_test {
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
