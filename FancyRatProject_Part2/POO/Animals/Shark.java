public class Shark extends Animal {
    // Define private attributes of the class
    private String livingArea;
    private int size;

    // Define the constructor
    public Shark(String name, String breed, String species, String skinColor, boolean isTerrestrial, String livingArea,
            int size) {
        super(name, breed, species, skinColor, isTerrestrial); // pass parameters to the superclass constructor
        this.livingArea = livingArea;
        this.size = size;
    }

    // Define get and set attributes
    public String getLivingArea() {
        return livingArea;
    }

    public void setLivingArea(String livingArea) {
        this.livingArea = livingArea;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    @Override
    public String toString() {
        return super.toString() + String.format(", livingArea=%s, size=%d", livingArea, size);
    }
}
