// Define the abstract builder class
abstract class HouseBuilder {
    protected int bedrooms;
    protected int bathrooms;
    protected int squareFeet;

    protected HouseBuilder(int bedrooms, int bathrooms, int squareFeet) {
        this.bedrooms = bedrooms;
        this.bathrooms = bathrooms;
        this.squareFeet = squareFeet;
    }

    protected abstract House build();
}

class SmallHouseBuilder extends HouseBuilder {
    SmallHouseBuilder(int bedrooms, int bathrooms, int squareFeet) {
        super(bedrooms, bathrooms, squareFeet);
    }

    @Override
    public House build() {
        return new SmallHouse(bedrooms, bathrooms, squareFeet);
    }
}

class MediumHouseBuilder extends HouseBuilder {
    MediumHouseBuilder(int bedrooms, int bathrooms, int squareFeet) {
        super(bedrooms, bathrooms, squareFeet);
    }

    @Override
    public House build() {
        return new MediumHouse(bedrooms, bathrooms, squareFeet);
    }
}

// Define the abstract house class
abstract class House {
    protected abstract int getBedrooms();

    protected abstract int getBathrooms();

    protected abstract int getSquareFeet();
}

// Define the concrete house classes
class SmallHouse extends House {
    private int bedrooms;
    private int bathrooms;
    private int squareFeet;

    // Fields to store house attributes
    SmallHouse(int bedrooms, int bathrooms, int squareFeet) {
        this.bedrooms = bedrooms;
        this.bathrooms = bathrooms;
        this.squareFeet = squareFeet;
    }

    // Implementation of abstract methods
    @Override
    public int getBedrooms() {
        return bedrooms;
    }

    @Override
    public int getBathrooms() {
        return bathrooms;
    }

    @Override
    public int getSquareFeet() {
        return squareFeet;
    }
}

class MediumHouse extends House {
    private int bedrooms;
    private int bathrooms;
    private int squareFeet;

    MediumHouse(int bedrooms, int bathrooms, int squareFeet) {
        this.bedrooms = bedrooms;
        this.bathrooms = bathrooms;
        this.squareFeet = squareFeet;
    }

    @Override
    public int getBedrooms() {
        return bedrooms;
    }

    @Override
    public int getBathrooms() {
        return bathrooms;
    }

    @Override
    public int getSquareFeet() {
        return squareFeet;
    }
}