public class Trailer implements Box {
    private int amountOfItems;
    private double weight;
    private String content;

    public Trailer(int amountOfItems, double weight, String content) {
        this.amountOfItems = amountOfItems;
        this.weight = weight;
        this.content = content;
    }

    public int getAmountOfItems() {
        return amountOfItems;
    }

    public double getWeight() {
        return weight;
    }

    public String getContent() {
        return content;
    }

    @Override
    public void printAmountOfItems() {
        System.out.println("This trailer has: " + amountOfItems + " items.");
    }

    @Override
    public void printWeight() {
        System.out.println("This trailer weighs: " + weight + " kg.");
    }

    @Override
    public void printContent() {
        System.out.println("This trailer contains: " + content + " items.");
    }
}
