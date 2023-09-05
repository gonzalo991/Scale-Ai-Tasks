// Define a class for creating a FoodDrinkBuilder
class FoodDrinkBuilder {
    constructor() {
        this.food = []; // Array to store food items
        this.drinks = []; // Array to store drink items
    }

    // Method to add a food item to the builder's food list
    addFood(food) {
        try {
            if (isValidFood(food)) {
                this.food.push(food);
                return this; // Returning 'this' allows for method chaining
            } else {
                throw new Error("Invalid food item");
            }
        } catch (error) {
            console.error(error.message);
            return this;
        }
    }

    // Method to add a drink item to the builder's drink list
    addDrink(drink) {
        try {
            if (isValidDrink(drink)) {
                this.drinks.push(drink);
                return this; // Returning 'this' allows for method chaining
            } else {
                throw new Error("Invalid drink item");
            }
        } catch (error) {
            console.error(error.message);
            return this;
        }
    }

    // Method to build the final order object with food and drink lists
    buildOrder() {
        return {
            food: this.food,
            drinks: this.drinks,
        };
    }

    // Method to clear the food and drink lists
    clearLists() {
        this.food = [];
        this.drinks = [];
    }
}

// Function to check if a food item is valid
function isValidFood(food) {
    const validFoods = ["pizza", "hamburger"];
    return validFoods.includes(food);
}

// Function to check if a drink item is valid
function isValidDrink(drink) {
    const validDrinks = ["cola", "beer"];
    return validDrinks.includes(drink);
}

// Example usage
const builder = new FoodDrinkBuilder();
builder.addFood("pizza");
builder.addFood("hamburger");
builder.addDrink("cola");
builder.addDrink("beer");

// Build the order object using the builder
const order = builder.buildOrder();

// Print the order
console.log(order);

// Clear the food and drink lists
builder.clearLists();