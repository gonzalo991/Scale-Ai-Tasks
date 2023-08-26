public class SoftDrinks {
    public static void main(String[] args) {
        Truck truck = new Truck(100, 10, "Soft drinks");
        truck.printAmountOfItems();
        truck.printWeight();
        truck.printContent();

        Trailer trailer = new Trailer(50, 5, "Coca-Cola");
        truck.addTrailer(trailer);
        truck.printAmountOfItems();
        truck.printWeight();
        truck.printContent();

        Trailer trailer2 = new Trailer(25, 3, "Pepsi");
        truck.addTrailer(trailer2);
        truck.printAmountOfItems();
        truck.printWeight();
        truck.printContent();
    }
}
