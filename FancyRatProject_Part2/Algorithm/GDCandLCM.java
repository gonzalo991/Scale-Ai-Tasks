// Define a class named GCDandLCM
public class GCDandLCM {

    // Method to calculate the Greatest Common Divisor (GCD) using the Euclidean algorithm
    public static int gcd(int a, int b) {
    
    // Base case: if b is 0, the GCD is found and we return a
    if (b == 0) {
    return a;
    }
    
    // Recursive case: continue calculating GCD using remainder
    return gcd(b, a % b);
    }
    
    // Method to calculate the Least Common Multiple (LCM)
    public static int lcm(int a, int b) {
    
    // LCM is calculated by dividing the product of a and b by their GCD
    return (a * b) / gcd(a, b);
    }
    
    // Main method, entry point of the program
    public static void main(String[] args) {
    
    // Initialize two integers a and b with values 5 and 7
    int a = 5;
    int b = 7;
    
    // Call gcd method to calculate GCD of a and b
    int gcd = gcd(a, b);
    
    // Call lcm method to calculate LCM of a and b
    int lcm = lcm(a, b);
    
    // Print the calculated GCD and LCM to the console
    System.out.println("GCD: " + gcd);
    System.out.println("LCM: " + lcm);
    }
}