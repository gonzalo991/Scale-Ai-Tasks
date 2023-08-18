public class Account {
    private int clientId;
    private static int clientCounter;
    private String name;
    private String surname;
    private int quantity;

    // Empty constructor
    public Account() {
        this.clientId = ++Account.clientCounter;
    }

    // Parameterised constructor
    public Account(String name, String surname, int quantity) {
        this();
        this.name = name;
        this.surname = surname;
        this.quantity = quantity;
    }

    // Getters and Setters
    public int getClientId() {
        return clientId;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    // Methods
    public void addMoney(int money) { // Adds money to the account
        this.quantity += money;
        System.out.println("Processing...");
        System.out.println("You've added money to your account : $ " + quantity + " .");
    }

    public int subtractMoney(int money) { // Extracts money from the account
        if (quantity > 0 && quantity > money) {
            this.quantity -= money;
            System.out.println("Processing...");
            System.out.println("You've substtacted money from your account: $" + quantity + " .");
            return this.quantity;
        } else {
            System.out.println("Not enough money");
            return this.quantity;
        }
    }

    public String getAccountBalance() { // Ask for the left money in the account
        return "$ " + this.quantity + " is the current balance of your account";
    }

    // To String method, print the values of the object
    @Override
    public String toString() {
        return "Account{" +
                "clientId='" + clientId + '\'' +
                ", name='" + name + '\'' +
                ", surname='" + surname + '\'' +
                ", quantity=" + quantity +
                '}';
    }
}