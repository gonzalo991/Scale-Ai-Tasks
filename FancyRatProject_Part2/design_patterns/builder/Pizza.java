// Define the abstract pizza builder class
abstract class PizzaBuilder {
    protected int crustThickness;
    protected int crustDiameter;
    protected int cheeseAmount;
    protected int sauceAmount;
    protected int toppingsAmount;

    public PizzaBuilder crustThickness(int crustThickness) {
        this.crustThickness = crustThickness;
        return this;
    }

    public PizzaBuilder crustDiameter(int crustDiameter) {
        this.crustDiameter = crustDiameter;
        return this;
    }

    public PizzaBuilder cheeseAmount(int cheeseAmount) {
        this.cheeseAmount = cheeseAmount;
        return this;
    }

    public PizzaBuilder sauceAmount(int sauceAmount) {
        this.sauceAmount = sauceAmount;
        return this;
    }

    public PizzaBuilder toppingsAmount(int toppingsAmount) {
        this.toppingsAmount = toppingsAmount;
        return this;
    }

    public abstract Pizza build();
}

// Define the concrete pizza builder classes
class ThinCrustPizzaBuilder extends PizzaBuilder {
    @Override
    public Pizza build() {
        return new ThinCrustPizza(crustThickness, crustDiameter, cheeseAmount, sauceAmount, toppingsAmount);
    }
}

class ThickCrustPizzaBuilder extends PizzaBuilder {
    @Override
    public Pizza build() {
        return new ThickCrustPizza(crustThickness, crustDiameter, cheeseAmount, sauceAmount, toppingsAmount);
    }
}

// Define the abstract pizza class
abstract class Pizza {
    protected int crustThickness;
    protected int crustDiameter;
    protected int cheeseAmount;
    protected int sauceAmount;
    protected int toppingsAmount;

    public abstract String getPizzaType();
}

// Define the concrete pizza classes
class ThinCrustPizza extends Pizza {
    ThinCrustPizza(int crustThickness, int crustDiameter, int cheeseAmount, int sauceAmount, int toppingsAmount) {
        this.crustThickness = crustThickness;
        this.crustDiameter = crustDiameter;
        this.cheeseAmount = cheeseAmount;
        this.sauceAmount = sauceAmount;
        this.toppingsAmount = toppingsAmount;
    }

    @Override
    public String getPizzaType() {
        return "Thin Crust";
    }
}

class ThickCrustPizza extends Pizza {
    ThickCrustPizza(int crustThickness, int crustDiameter, int cheeseAmount, int sauceAmount, int toppingsAmount) {
        this.crustThickness = crustThickness;
        this.crustDiameter = crustDiameter;
        this.cheeseAmount = cheeseAmount;
        this.sauceAmount = sauceAmount;
        this.toppingsAmount = toppingsAmount;
    }

    @Override
    public String getPizzaType() {
        return "Thick Crust";
    }
}