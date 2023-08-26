from abc import ABC, abstractmethod

# Abstract base class for weapons
class AbstractWeapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def equip(self):
        pass

    @abstractmethod
    def unequip(self):
        pass

    @abstractmethod
    def get_attack_range(self):
        pass

# Concrete weapon classes
class Staff(AbstractWeapon):
    def __init__(self, weapon_name, magic_force, attack_range):
        self.weapon_name = weapon_name
        self.magic_force = magic_force
        self.attack_range = attack_range

    def attack(self):
        print("Staff attack")

    def equip(self):
        print(f"Equipping {self.weapon_name}, Attack range: {self.attack_range}, Magic Force: {self.magic_force}")

    def unequip(self):
        print(f"Staff {self.weapon_name} unequipped...")

    def get_attack_range(self):
        return self.attack_range

# Concrete weapon class Sword (similar to Staff, with different properties)
class Sword(AbstractWeapon):
    def __init__(self, weapon_name, force, attack_range):
        self.weapon_name = weapon_name
        self.force = force
        self.attack_range = attack_range

    def attack(self):
        print("Sword attack")

    def equip(self):
        print(f"Equiping {self.weapon_name}, Attack range: {self.attack_range}, Force: {self.force}")
    
    def unequip(self):
        print("Sword unequiped...")

    def get_attack_range(self):
        return self.attack_range

# Concrete weapon class Bow (similar to Staff, with different properties)
class Bow(AbstractWeapon):
    def __init__(self, weapon_name, force, attack_range):
        self.weapon_name = weapon_name
        self.force = force
        self.attack_range = attack_range

    def attack(self):
        print("Bow attack")

    def equip(self):
        print(f"Equiping {self.weapon_name}, Attack range: {self.attack_range},  Force: {self.force}")

    def unequip(self):
        print("Bow unequiped...")

    def get_attack_range(self):
        return self.attack_range

# Factory class to create weapons
class WeaponFactory:
    @staticmethod
    def create_staff(weapon_name, magic_force, attack_range):
        try:
            return Staff(weapon_name, magic_force, attack_range)  # Try creating a Staff object
        except Exception as e:
            print(f"Error creating staff: {e}")
            return None  # Return None if creation fails

    @staticmethod
    def create_sword(weapon_name, force, attack_range):
        try:
            return Sword(weapon_name, force, attack_range)  # Try creating a Sword object
        except Exception as e:
            print(f"Error creating sword: {e}")
            return None  # Return None if creation fails

    @staticmethod
    def create_bow(weapon_name, force, attack_range):
        try:
            return Bow(weapon_name, force, attack_range)  # Try creating a Bow object
        except Exception as e:
            print(f"Error creating bow: {e}")
            return None  # Return None if creation fails
        
# Usage example
staff = WeaponFactory.create_staff("Rylai Staff", 10, 0.9)
sword = WeaponFactory.create_sword("Flame Sword", 90, 0.1)
bow = WeaponFactory.create_bow("Long Strnghened Bow", 400, 2.5)

staff.equip()
staff.attack()
staff.unequip()

sword.equip()
sword.attack()
sword.unequip()

bow.equip()
bow.attack()
bow.unequip()