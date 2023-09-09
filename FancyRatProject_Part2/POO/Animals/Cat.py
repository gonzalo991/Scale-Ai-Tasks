from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def sound(self):
        pass

class Cat(Animal):
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def sound(self):
        return "Meow"

    def run(self):
        return f"{self.name} is running.."
    
    def sleep(self):
        return f"{self.name} is sleeping grrrr..."
    
    def eat(self):
        return f"{self.name} is eating..."
    
# Example usage
cat = Cat("Whiskers", 4, "Persian")
print(cat.name)  # Output: Whiskers
print(cat.age)  # Output: 4
print(cat.breed)  # Output: Persian
print(cat.sound())  # Output: Meow
print(cat.eat()) # Output Whiskers is eating...
print(cat.run()) # Output: Whiskers is running..
print(cat.sleep()) # Output : Whiskers is sleeping grrrr...