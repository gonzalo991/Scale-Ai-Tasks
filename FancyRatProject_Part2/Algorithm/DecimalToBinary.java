// Define a class named DecimalToBinary
public class DecimalToBinary {

    // Method to convert a decimal integer to a binary string
    public static String decimalToBinary(int decimal) {
    StringBuilder binary = new StringBuilder();
    
    // Convert the decimal number to binary representation
    while (decimal > 0) {
    binary.append(decimal % 2); // Append the remainder (0 or 1) to the binary representation
    decimal /= 2; // Divide the decimal number by 2 to continue conversion
    }
    
    // Handle the case where the input decimal is 0
    if (binary.length() == 0) {
    binary.append('0');
    }
    
    return binary.reverse().toString(); // Reverse the binary representation and return as string
    }
    
    // Method to convert a binary string to a decimal integer
    public static int binaryToDecimal(String binary) {
    int decimal = 0;
    int length = binary.length();
    
    // Convert binary to decimal representation
    for (int i = length - 1; i >= 0; i--) {
    if (binary.charAt(i) == '1') {
    decimal += Math.pow(2, length - 1 - i); // Add 2 raised to the power of position
    }
    }
    
    return decimal;
    }
    
    // Main method, entry point of the program
    public static void main(String[] args) {
    System.out.println("Binary Representation of 5: " + decimalToBinary(5));
    System.out.println("Decimal Representation of 101: " + binaryToDecimal("101"));
    }
}