from abc import ABC, abstractmethod
from MediaItem import MediaItem

class AudioBook(MediaItem):
    def __init__(self, title, duration, author, ISBN):
        super().__init__(title, duration)
        self._author = author
        self._ISBN = ISBN

    def __str__(self):
        return f"[ {super().__str__()}, Author: {self._author}, ISBN: {self._ISBN} ]"

    def play(self):
        print("Playing audio book...")

    def stop(self):
        print("Stopping audio book...")

    def display_info(self):
        print("Title:", self.title)
        print("Duration:", self.duration)