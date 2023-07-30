package FancyRatProject;
public class Test {
    public static void main(String args[]) {
        String str1 = "Hello";
        String str2 = "World!";
        System.out.println("The hash code of str1 is: " + str1.hashCode());
        System.out.println("\nThe hash code of str2 is: " + str2.hashCode());
        String str3 = "Same value";
        String str4 = "Same value";
        System.out.println("The hash code of str3 is: " + str3.hashCode());
        System.out.println("\nThe hash code of str4 is: " + str4.hashCode());
    }
}