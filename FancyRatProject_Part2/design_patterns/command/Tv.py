from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Receiver class
class TV:
    def __init__(self):
        self._volume = 0

    def turn_on(self):
        print("TV is on")

    def turn_off(self):
        print("TV is off")

    def change_volume(self, volume):
        self._volume = volume
        print(f"TV volume is set to {self._volume}")

    def undo_change_volume(self, volume):
        self._volume = volume
        print(f"TV volume is reverted to {self._volume}")

# Concrete command classes
class TurnOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_on()

    def undo(self):
        self.tv.turn_off()

class TurnOffCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.turn_off()

    def undo(self):
        self.tv.turn_on()

class ChangeVolumeCommand(Command):
    def __init__(self, tv):
        self.tv = tv
        self.prev_volume = None
        self.current_volume = None

    def execute(self, volume):
        self.prev_volume = self.tv._volume
        self.current_volume = volume
        self.tv.change_volume(volume)

    def undo(self):
        if self.prev_volume is not None:
            self.tv.undo_change_volume(self.prev_volume)

# Invoker class
class RemoteControl:
    def __init__(self):
        self.command = None
        self.history = []

    def set_command(self, command):
        self.command = command

    def press_button(self, *args, **kwargs):
        self.history.append(self.command)
        self.command.execute(*args, **kwargs)

    def press_button_undo(self):
        if len(self.history) > 0:
            self.command = self.history.pop()
            self.command.undo()

# Client code
tv = TV()
turn_on = TurnOnCommand(tv)
turn_off = TurnOffCommand(tv)
change_volume = ChangeVolumeCommand(tv)

remote = RemoteControl()

remote.set_command(turn_on)
remote.press_button() # Outputs: TV is on

remote.set_command(change_volume)
remote.press_button(25) # Outputs: TV volume is set to 25

remote.press_button_undo() # Outputs: TV volume is reverted to 25

remote.set_command(turn_off)
remote.press_button() # Outputs: TV is off

remote.press_button_undo() # Outputs: TV is on