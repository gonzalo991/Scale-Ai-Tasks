class House {
    constructor() {
        // Initialize attributes with default values
        this.numberOfRooms = 0;
        this.numberOfBathrooms = 0;
        this.hasGarage = false;
        this.hasHall = false;
        this.hasLivingRoom = false;
        this.hasGarden = false;
    }

    // Singleton instance creation
    static getInstance() {
        if (!House.instance) {
            House.instance = new House();
        }
        return House.instance;
    }

    // Method to set the attributes of the house
    setAttributes(rooms, bathrooms, garage, hall, livingRoom, garden) {
        this.numberOfRooms = rooms;
        this.numberOfBathrooms = bathrooms;
        this.hasGarage = garage;
        this.hasHall = hall;
        this.hasLivingRoom = livingRoom;
        this.hasGarden = garden;
    }

    // Method to display the attributes of the house
    displayAttributes() {
        console.log('House Attributes:');
        console.log(`Number of Rooms: ${this.numberOfRooms}`);
        console.log(`Number of Bathrooms: ${this.numberOfBathrooms}`);
        console.log(`Has Garage: ${this.hasGarage}`);
        console.log(`Has Hall: ${this.hasHall}`);
        console.log(`Has Living Room: ${this.hasLivingRoom}`);
        console.log(`Has Garden: ${this.hasGarden}`);
    }

    // Method to calculate the area of the house
    calculateArea(size) {
        let area = size * this.numberOfRooms;
        return area;
    }
}

// Usage
const myHouse = House.getInstance(); // Get the singleton instance of House
myHouse.setAttributes(3, 2, true, true, true, true); // Set attributes
myHouse.displayAttributes(); // Display house attributes

const area = myHouse.calculateArea(500);
console.log('Area of the house: ' + area);