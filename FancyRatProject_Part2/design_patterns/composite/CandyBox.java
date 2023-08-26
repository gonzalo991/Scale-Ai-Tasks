public class CandyBox implements Box {
    // Define attributes
    private int amountOfCandies;
    private double weight;
    private String content;

    // Class constructor
    public CandyBox(int amountOfCandies, double weight, String content){
        this.amountOfCandies = amountOfCandies;
        this.weight = weight;
        this.content = content;
    }

    // Define getters and setters
    public int getAmountOfCandies(){
        return this.amountOfCandies;
    }

    public void setAmountOfCandies(int amountOfCandies){
        this.amountOfCandies = amountOfCandies;
    }

    public double getWeight(){
        return this.weight;
    }

    public void setWeight(double weight){
        this.weight = weight;
    }

    public String getContent(){
        return this.content;
    }

    public void setContent (String content){
        this.content = content;
    }

    @Override
    public void printAmountOfItems() {
        System.out.println("This box has : "+this.getAmountOfCandies()+" Candies.");
    }

    @Override
    public void printWeight() {
        System.out.println("this box weighs: "+this.getWeight()+ " Kg.");
    }

    @Override
    public void printContent() {
        System.out.println("This box contains: "+this.getContent());
    }
    
}
