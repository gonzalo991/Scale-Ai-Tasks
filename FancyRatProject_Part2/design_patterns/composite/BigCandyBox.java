import java.util.ArrayList;
import java.util.List;

public class BigCandyBox implements Box{
    private String candyContent;
    private double weight;
    private List<CandyBox> items = new ArrayList<>();

    public BigCandyBox(String candyContent){
        this.candyContent = candyContent;
    }

    public String getCandyContet(){
        return this.candyContent;
    }

    public void setCandyContent(String candyContent){
        this.candyContent = candyContent;
    }

    public int getAmountOfItems(){
        return items.size();
    }

    public void addItem(CandyBox item){
        items.add(item);
    }

    public double getWeight(){
        for (CandyBox box : items) {
            this.weight += box.getWeight();
        }
        return this.weight;
    }
    
    public void setWeight(double weight){
        this.weight = weight;
    }

    @Override
    public void printAmountOfItems() {
        System.out.println("This box has: "+this.getAmountOfItems()+ " boxes.");
    }

    @Override
    public void printWeight() {
        System.out.println("This box weighs: "+this.getWeight()+" Kg.");
    }

    @Override
    public void printContent() {
        System.out.println("This box contains: "+this.getCandyContet()+ " boxes.");
    }
}
