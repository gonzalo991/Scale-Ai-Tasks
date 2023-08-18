from abc import ABC, abstractmethod

class MediaItem:
    def __init__(self, title, duration):
        self._title = title
        self._duration = duration

    def __str__(self):
        return f"[ Títle: {self._title}, Duration: {self._duration} ]"

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def display_info(self):
        pass