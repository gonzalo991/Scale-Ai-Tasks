# Create the bedroom class
class Bedroom:
    # Define the dunder init method
    def __init__(self, beds, bedside_table, air_conditioner, closet ):
        self._beds = beds
        self._bedside_table = bedside_table
        self._air_conditioner = air_conditioner
        self._closet = closet

    # Define the dunder str method to display the details of the class
    def __str__(self) -> str:
        return f"[ Beds: {self._beds}, Bedside Table: {self._bedside_table}, Air Conditioner: {self._air_conditioner}, Closets : {self._closet} ] "

    # Define getters and setter with the @property annotation
    @property
    def beds(self):
        return self._beds

    @beds.setter
    def beds(self, more_beds):
        self._beds = more_beds

    @property
    def bedside_table(self):
        return self._bedside_table

    @bedside_table.setter
    def bedside_table(self, more_bedsidetables):
        self._bedside_table = more_bedsidetables

    @property
    def air_conditioner(self):
        return self._air_conditioner

    @air_conditioner.setter
    def air_conditioner(self, is_air_conditioner):
        self._air_conditioner = is_air_conditioner

    @property
    def closet(self):
        return self._closet

    @closet.setter
    def closet(self, new_closet):
        self._closet = new_closet

# Example of usage

# Define a new Bedroom class
my_bedroom = Bedroom(1,True, True, 1)

# Print the details of the bedroom
print(my_bedroom) # [ Beds: 1, Bedside Table: True, Air Conditioner: True, Closets: 1 ]