from abc import ABC, abstractmethod

class GameAI(ABC):

    @abstractmethod
    def collect_resources(self):
        pass

    @abstractmethod
    def build_structures(self):
        pass

    @abstractmethod
    def build_units(self):
        pass

    @abstractmethod
    def send_scouts(self, position):
        pass

    @abstractmethod
    def send_warriors(self, position):
        pass

    def turn(self):
        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def attack(self):
        enemy = self.closest_enemy()
        if enemy is None:
            self.send_scouts("center")
        else:
            self.send_warriors(enemy)

    def closest_enemy(self):
        # Placeholder for getting closest enemy
        return None

class OrcsAI(GameAI):
    def __init__(self):
        self.resources = 100  # Orcs start with 100 resources
        self.built_structures = []
        self.scouts = []
        self.warriors = []

    def collect_resources(self):
        # Collect resources based on the built structures
        for s in self.built_structures:
            self.resources += s.collect()

    def build_structures(self):
        self.build_farms()
        self.build_barracks()
        self.build_fortress()

    def build_farms(self):
        if self.resources > 10:
            # Build farms
            self.built_structures.append("farm")
            self.resources -= 10

    def build_barracks(self):
        if self.resources > 20:
            # Build barracks
            self.built_structures.append("barracks")
            self.resources -= 20

    def build_fortress(self):
        if self.resources > 30:
            # Build fortress
            self.built_structures.append("fortress")
            self.resources -= 30

    def build_units(self):
        if self.resources > 50:  # Assume plenty of resources means more than 50
            if not self.scouts:  # If there are no scouts
                # Create a scout and add it to the scouts group
                self.scouts.append("scout")
                self.resources -= 10  # Let's say building a scout costs 10 resources
            else:
                # Create a warrior and add it to the warriors group
                self.warriors.append("warrior")
                self.resources -= 20  # Let's say building a warrior costs 20 resources

    def send_scouts(self, position):
        if self.scouts:
            # Send scouts to position
            print(f"Sending scouts to {position}")

    def send_warriors(self, position):
        if len(self.warriors) > 5:  # if there are more than 5 warriors
            # Send warriors to position
            print(f"Sending warriors to {position}")

class MonstersAI(GameAI):
    def collect_resources(self):
        pass  # Monsters do not collect resources.

    def build_structures(self):
        pass  # Monsters do not build structures.

    def build_units(self):
        pass  # Monsters do not build units.