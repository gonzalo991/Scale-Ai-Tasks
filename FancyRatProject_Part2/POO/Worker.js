class Worker {

    constructor(name, age, gender, paymentPerHour, paymentPerWeek) {
        if (new.target === Worker) {
            throw new Error("Cannot instantiate an abstract class.");
        }
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.paymentPerHour = paymentPerHour;
        this.paymentPerWeek = paymentPerWeek;
    }

    calculateWeeklyPayment() {
        throw new Error("Subclasses must implement the 'calculateWeeklyPayment' method.");
    }
}

class MarketWorker extends Worker {
    constructor(name, age, gender, paymentPerHour, paymentPerWeek, weeklyHours) {
        super(name, age, gender, paymentPerHour, paymentPerWeek);
        this.weeklyHours = weeklyHours;
    }

    // Implementing the abstract method with custom calculation
    calculateWeeklyPayment() {
        return this.paymentPerHour * this.weeklyHours;
    }

    // Display details of the market worker
    displayDetails() {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
        console.log(`Gender: ${this.gender}`);
        console.log(`Payment per hour: ${this.paymentPerHour}`);
        console.log(`Payment per week: ${this.paymentPerWeek}`);
        console.log(`Weekly hours: ${this.weeklyHours}`);
    }

    // Calculate yearly payment for the market worker
    calculateYearlyPayment() {
        return this.paymentPerHour * this.weeklyHours * 52; // 52 weeks in a year
    }
}

// Example usage
const marketWorker = new MarketWorker("John", 28, "Male", 15, 0, 40);
const weeklyPayment = marketWorker.calculateWeeklyPayment();
console.log(`Weekly payment for ${marketWorker.name}: $${weeklyPayment}`);
marketWorker.displayDetails();

// Update payment per hour
marketWorker.updatePaymentPerHour(25);
console.log(marketWorker.displayDetails());

// Calculate yearly payment
const yearlyPayment = marketWorker.calculateYearlyPayment();
console.log(`Yearly payment for ${marketWorker.name}: $${yearlyPayment}`);
