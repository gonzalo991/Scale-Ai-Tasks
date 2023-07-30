package FancyRatProject;
public class Monitor {

    private final int idMonitor;
    private static int monitorCounter;
    private String brand;
    private String size;

    private Monitor() {
        this.idMonitor = ++Monitor.monitorCounter;
    }

    public Monitor(String brand, String size) {
        this(); // llamada al constructor vacio
        this.brand = brand;
        this.size = size;
    }

    public String getBrand() {
        return this.brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getSize() {
        return this.size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    // Ingresamos manualmente el getIdMonitor
    public int getIdMonitor() {
        return this.idMonitor;
    }

    @Override
    public String toString() {
        return "Monitor{" + "idMonitor = " + idMonitor + ", Brand = " + brand + ", size = " + size + '}';
    }

}