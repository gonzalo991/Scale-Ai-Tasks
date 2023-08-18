from abc import ABC, abstractmethod
from MediaItem import MediaItem # Import the base abstract class

# Define a Movie class that inherits from the MediaItem abstract class
class Movie(MediaItem):
    def __init__(self, title, duration, director, year):
        # Call the constructor of the base class using super()
        super().__init__(title, duration)

        # Initialize additional attributes specific to the Movie class
        self._director = director
        self._year = year

    def __str__(self):
        # Customize the string representation of the Movie instance
        return f"[ {super().__str__()}, Director: {self._director}, Year: {self._year} ]"

    def play(self):
        # Implement the play method from the abstract base class
        print("Playing movie...")

    def stop(self):
        # Define a custom method for stopping the movie
        print("Stopping movie...")

    def display_info(self):
        # Implement the display_info method from the abstract base class
        print("Title:", self.title)
        print("Duration:", self.duration)
        print("Director:", self._director)
        print("Year:", self._year)