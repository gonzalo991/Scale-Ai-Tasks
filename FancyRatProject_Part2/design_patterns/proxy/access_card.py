from abc import ABC, abstractmethod

# Step 1: Create an abstract class or interface for AccessCard.
class AccessCard(ABC):
    @abstractmethod
    def grant_access(self):
        pass

# Step 2: Create a RealAccessCard class that implements the interface.
class RealAccessCard(AccessCard):
    def __init__(self, employee):
        self.employee = employee

    def grant_access(self):
        try:
            print(f"Access granted for {self.employee.name} with ID: {self.employee.id}")
        except AttributeError:
            print("Error: Employee information not found.")

# Step 3: Create an AccessCardProxy class that also implements the interface.
class AccessCardProxy(AccessCard):
    def __init__(self, employee):
        self.employee = employee
        self._real_access_card = None

    def grant_access(self):
        if self._real_access_card is None:
            self._real_access_card = RealAccessCard(self.employee)
        try:
            print("Proxy: Logging access request.")
            self._real_access_card.grant_access()
            print("Proxy: Logging access request completed.")
        except AttributeError:
            print("Error: Employee information not found.")

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Step 4: Client code interacts with the AccessCardProxy, not the RealAccessCard.
def main():
    employee1 = Employee(1, "John Smith")
    employee2 = Employee(2, "Jane Doe")

    proxy1 = AccessCardProxy(employee1)
    proxy2 = AccessCardProxy(employee2)

    proxy1.grant_access()  # Output: Proxy: Logging access request. Access granted for John Smith with ID: 1 Proxy: Logging access request completed.
    proxy2.grant_access()  # Output: Proxy: Logging access request. Access granted for Jane Doe with ID: 2 Proxy: Logging access request completed.

if __name__ == "__main__":
    main()