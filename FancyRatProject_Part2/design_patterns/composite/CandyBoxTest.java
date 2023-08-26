public class CandyBoxTest {
    public static void main(String[] args) {
        // Chocolate boxes
        CandyBox chocolateBox = new CandyBox(24, 1.2, "Chocolates");
        chocolateBox.printAmountOfItems();
        chocolateBox.printWeight();
        chocolateBox.printContent();

        // Candy pop boxes
        CandyBox candyPopBox = new CandyBox(50, 0.500, "Candy Pops");
        candyPopBox.printAmountOfItems();
        candyPopBox.printWeight();
        candyPopBox.printContent();

        // Big vox compisite class usage
        BigCandyBox bigBox = new BigCandyBox("Chocolates and Candy Pops");
        bigBox.addItem(chocolateBox);
        bigBox.addItem(candyPopBox);
        bigBox.printAmountOfItems();
        bigBox.printWeight();
        bigBox.printContent();
    }
}
