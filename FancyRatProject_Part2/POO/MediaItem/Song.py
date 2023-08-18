from abc import ABC, abstractmethod
from MediaItem import MediaItem # Import the base abstract class

# Define a Song class that inherits from the MediaItem abstract class
class Song(MediaItem):
    def __init__(self, title, artist, album, duration):
        # Call the constructor of the base class using super()
        super().__init__(title, duration)

        # Initialize additional attributes specific to the Song class
        self._artist = artist
        self._album = album

    def __str__(self):
        # Customize the string representation of the Song instance
        return f"[ {super().__str__()}, Artist: {self._artist}, Album: {self._album} ]"

    def play(self):
        # Implement the play method from the abstract base class
        print("Playing song...")

    def stop(self):
        # Define a custom method for stopping the song
        print("Stopping song...")

    def display_info(self):
        # Implement the display_info method from the abstract base class
        print("Title: ", self._title)
        print("Artist: ", self._artist)
        print("Album:", self._album)
        print("Duration:", self._duration)