// Define an Enum to represent attributes with encapsulated values
enum Attribute {
    STRENGTH(10),
    ARMOR(10),
    SPEED(10),
    STAMINA(10);

    private int value;

    Attribute(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

// Define an Enum to represent weapon types
enum Weapon {
    SWORD,
    BOW,
    AXE,
    MAGIC_STAFF
}

// Abstract product interface for characters
interface Character {
    // Methods that character classes must implement
    void attack();
    void rest();
    void levelUp(Attribute attribute);
    void equipWeapon(Weapon weapon); // Method to equip a weapon
    String getInfo();
}

// Concrete product class for Dragon Rider character
class DragonRider implements Character {
    private int strength;
    private int armor;
    private int speed;
    private int stamina;
    private Weapon equippedWeapon; // Track the equipped weapon

    // Constructor to initialize attributes
    public DragonRider(int strength, int armor, int speed, int stamina) {
        this.strength = strength;
        this.armor = armor;
        this.speed = speed;
        this.stamina = stamina;
    }

    @Override
    public void attack() {
        if (equippedWeapon != null) {
            System.out.println("Dragon Rider attacks with " + equippedWeapon + "!");
        } else {
            System.out.println("Dragon Rider attacks with fire!");
        }
    }

    @Override
    public void rest() {
        System.out.println("Dragon Rider rests to regain stamina.");
    }

    @Override
    public void levelUp(Attribute attribute) {
        int increment = attribute.getValue();
        switch (attribute) {
            case STRENGTH:
                strength += increment;
                break;
            case ARMOR:
                armor += increment;
                break;
            case SPEED:
                speed += increment;
                break;
            case STAMINA:
                stamina += increment;
                break;
            default:
                // Handle the case where an invalid attribute is selected for leveling up
                System.out.println("Invalid attribute selected for level up.");
                throw new IllegalArgumentException("Invalid attribute selected for level up.");
        }
        System.out.println("Dragon Rider gains experience and improves " + attribute + " by " + increment + " points!");
    }

    @Override
    public void equipWeapon(Weapon weapon) {
        // Equip the specified weapon
        equippedWeapon = weapon;
        System.out.println("Dragon Rider equips a " + equippedWeapon + "!");
    }

    @Override
    public String getInfo() {
        String weaponInfo = (equippedWeapon != null) ? equippedWeapon.toString() : "None";
        return "Dragon Rider - Strength: " + strength + ", Armor: " + armor +
                ", Speed: " + speed + ", Stamina: " + stamina + ", Equipped Weapon: " + weaponInfo;
    }
}

// Abstract factory interface for creating characters
interface CharacterFactory {
    // Factory method to create characters
    Character createCharacter();
}

// Concrete factory class for creating Dragon Rider characters
class DragonRiderFactory implements CharacterFactory {
    @Override
    public Character createCharacter() {
        // Create and return a new Dragon Rider character with initial attribute values
        return new DragonRider(35, 15, 20, 30);
    }
}

public class Main {
    public static void main(String[] args) {
        try {
            // Create a Dragon Rider character using the Dragon Rider Factory
            CharacterFactory dragonRiderFactory = new DragonRiderFactory();
            Character dragonRider = dragonRiderFactory.createCharacter();

            // Interact with the character
            dragonRider.attack();
            dragonRider.equipWeapon(Weapon.SWORD); // Equip a weapon
            dragonRider.attack(); // Now, the character attacks with the equipped weapon
            dragonRider.rest();
            
            // Level up specific attributes
            dragonRider.levelUp(Attribute.STRENGTH); // Level up strength attribute by 10 points
            dragonRider.levelUp(Attribute.ARMOR); // Level up armor attribute by 10 points

            // Get and display character information
            System.out.println(dragonRider.getInfo());
        } catch (IllegalArgumentException e) {
            // Handle the case where an invalid attribute is selected for leveling up
            System.out.println(e.getMessage());
        }
    }
}
