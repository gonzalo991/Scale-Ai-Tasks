import java.util.ArrayList;
import java.util.List;

public class Truck implements Box {
    private int amountOfItems;
    private double weight;
    private String content;
    private List<Trailer> trailers = new ArrayList<>();

    public Truck(int amountOfItems, double weight, String content) {
        this.amountOfItems = amountOfItems;
        this.weight = weight;
        this.content = content;
    }

    public void addTrailer(Trailer trailer) {
        trailers.add(trailer);
    }

    public int getAmountOfItems() {
        int total = amountOfItems;
        for (Trailer trailer : trailers) {
            total += trailer.getAmountOfItems();
        }
        return total;
    }

    public double getWeight() {
        double total = weight;
        for (Trailer trailer : trailers) {
            total += trailer.getWeight();
        }
        return total;
    }

    public String getContent() {
        String content = this.content;
        for (Trailer trailer : trailers) {
            content += trailer.getContent();
        }
        return content;
    }

    @Override
    public void printAmountOfItems() {
        System.out.println("This truck has: " + getAmountOfItems() + " items.");
    }

    @Override
    public void printWeight() {
        System.out.println("This truck weighs: " + getWeight() + " kg.");
    }

    @Override
    public void printContent() {
        System.out.println("This truck contains: " + getContent() + " items.");
    }
}
