public class AccountTest {
    public static void main(String[] args) {
        Account account = new Account("John Smith", "Smith", 100);
        System.out.println("Account Balance: " + account.getAccountBalance());
        account.addMoney(50);
        System.out.println("Account Balance: " + account.getAccountBalance());
        account.subtractMoney(20);
        System.out.println("Account Balance: " + account.getAccountBalance());
    }
}