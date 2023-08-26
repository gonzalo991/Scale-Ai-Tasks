// Define the abstract car builder class
abstract class CarBuilder {
    protected String manufacturer;
    protected String model;
    protected String year;
    protected int horsepower;

    public CarBuilder manufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
        return this;
    }

    public CarBuilder model(String model) {
        this.model = model;
        return this;
    }

    public CarBuilder year(String year) {
        this.year = year;
        return this;
    }

    public CarBuilder horsepower(int horsepower) {
        this.horsepower = horsepower;
        return this;
    }

    public abstract Car build();
}

// Define the concrete car builder classes
class ToyotaBuilder extends CarBuilder {
    @Override
    public Car build() {
        return new Toyota(manufacturer, model, year, horsepower);
    }
}

class HondaBuilder extends CarBuilder {
    @Override
    public Car build() {
        return new Honda(manufacturer, model, year, horsepower);
    }
}

class NissanBuilder extends CarBuilder {
    @Override
    public Car build() {
        return new Nissan(manufacturer, model, year, horsepower);
    }
}

// Define the abstract car class
abstract class Car {
    protected String manufacturer;
    protected String model;
    protected String year;
    protected int horsepower;

    public abstract String getBrand();
}

// Define the concrete car classes
class Toyota extends Car {
    Toyota(String manufacturer, String model, String year, int horsepower) {
        this.manufacturer = manufacturer;
        this.model = model;
        this.year = year;
        this.horsepower = horsepower;
    }

    @Override
    public String getBrand() {
        return "Toyota";
    }
}

class Honda extends Car {
    Honda(String manufacturer, String model, String year, int horsepower) {
        this.manufacturer = manufacturer;
        this.model = model;
        this.year = year;
        this.horsepower = horsepower;
    }

    @Override
    public String getBrand() {
        return "Honda";
    }
}

class Nissan extends Car {
    Nissan(String manufacturer, String model, String year, int horsepower) {
        this.manufacturer = manufacturer;
        this.model = model;
        this.year = year;
        this.horsepower = horsepower;
    }

    @Override
    public String getBrand() {
        return "Nissan";
    }
}
