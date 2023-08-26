# Import the ABC (Abstract Base Class) module and the 'abstractmethod' decorator
from abc import ABC, abstractmethod

# Define an abstract base class 'AbstractProfessional' inheriting from ABC
class AbstractProfessional(ABC):
    # Constructor for initializing the name and specialty attributes
    def __init__(self, name, specialty):
        self._name = name
        self._specialty = specialty

    # Declare an abstract method 'get_name'
    @abstractmethod
    def get_name(self):
        pass

    # Declare an abstract method 'get_specialty'
    @abstractmethod
    def get_specialty(self):
        pass

# Concrete subclasses of 'AbstractProfessional' with implemented methods
class Doctor(AbstractProfessional):
    def get_name(self):
        return self._name

    def get_specialty(self):
        return self._specialty

class Lawyer(AbstractProfessional):
    def get_name(self):
        return self._name

    def get_specialty(self):
        return self._specialty

class Engineer(AbstractProfessional):
    def get_name(self):
        return self._name

    def get_specialty(self):
        return self._specialty

class SoftwareDeveloper(AbstractProfessional):
    def get_name(self):
        return self._name

    def get_specialty(self):
        return self._specialty

# Abstract base class for factories with a method 'create_professional'
class AbstractFactory(ABC):
    @abstractmethod
    def create_professional(self, name, specialty):
        pass

# Concrete subclasses of 'AbstractFactory' with implemented 'create_professional' method
class Hospital(AbstractFactory):
    def create_professional(self, name, specialty):
        return Doctor(name, specialty)

class LawFirm(AbstractFactory):
    def create_professional(self, name, specialty):
        return Lawyer(name, specialty)

class EngineeringFirm(AbstractFactory):
    def create_professional(self, name, specialty):
        return Engineer(name, specialty)

class SoftwareCompany(AbstractFactory):
    def create_professional(self, name, specialty):
        return SoftwareDeveloper(name, specialty)

# Function to get valid user input for the professional type
def get_valid_professional_type():
    while True:
        professional_type = input("Enter the professional type (Doctor, Lawyer, Engineer, SoftwareDeveloper): ").strip().lower()
        if professional_type in ["doctor", "lawyer", "engineer", "softwaredeveloper"]:
            return professional_type
        else:
            print("Invalid professional type. Please choose from Doctor, Lawyer, Engineer, or SoftwareDeveloper.")

# Function to get valid user input for the specialty
def get_valid_specialty():
    while True:
        specialty = input("Enter the specialty: ").strip()
        if specialty:
            return specialty
        else:
            print("Specialty cannot be empty. Please enter a valid specialty.")

# Usage of the program
if __name__ == "__main__":
    try:
        name = input("Plase enter the professional name: ")
        professional_type = get_valid_professional_type()
        specialty = get_valid_specialty()

        if professional_type == "doctor":
            factory = Hospital()
        elif professional_type == "lawyer":
            factory = LawFirm()
        elif professional_type == "engineer":
            factory = EngineeringFirm()
        elif professional_type == "softwaredeveloper":
            factory = SoftwareCompany()
        else:
            print("Invalid professional type.")
            exit()

        professional = factory.create_professional(name, specialty)
        print(f"{professional_type.capitalize()}: {professional.get_name()}, Specialty: {professional.get_specialty()}")

    except Exception as e:
        print("An error occurred:", str(e))