import java.util.Scanner;

public class SharkTest {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);

        System.out.println("Set the data of the animal");
        System.out.println("Name: ");
        String name = read.next();
        System.out.println("Breed: ");
        String breed = read.next();
        System.out.println("Species: ");
        String species = read.next();
        System.out.println("Skin Color: ");
        String skinColor = read.next();
        System.out.println("Is a terrestrial animal ?");
        boolean isTerrestrial = read.nextBoolean();
        System.out.println("Living Area: ");
        String livingArea = read.next();
        System.out.println("Size in meters: ");
        int size = read.nextInt();

        Shark sharky = new Shark(name, breed, species, skinColor, isTerrestrial, livingArea, size);

        System.out.println(sharky.toString());

    }
}
