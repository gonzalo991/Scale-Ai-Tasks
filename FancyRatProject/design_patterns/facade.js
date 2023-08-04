// ComplexSystem class
class ComplexSystem {
    // ... complex logic here ...
    operation1() {
    return "Complex operation1";
    }
    
    operation2() {
    return "Complex operation 2";
    }
    }
    
    // SimpleSystem class
    class SimpleSystem {
    // ... simple logic here ...
    operation() {
    return "Simple operation";
    }
    }
    
    // Facade class
    class Facade {
    constructor() {
    this.simpleSystem = new SimpleSystem();
    }
    
    simpleOperation() {
    return this.simpleSystem.operation();
    }
    }
    
    // complexAction function
    const complexAction = () => {
    return new ComplexSystem();
    };
    
    // Function simpleAction
    const simpleAction = () => {
    return new SimpleSystem();
    };
    
    // Main function
    const main = () => {
    const facade = new Facade();
    const complexSystem = complexAction();
    
    console.log("Simple operation:", facade.simpleOperation());
    console.log("Complex operation 1:", complexSystem.operation1());
    console.log("Complex operation 2:", complexSystem.operation2());
    };
    
    export { main, complexAction, simpleAction };