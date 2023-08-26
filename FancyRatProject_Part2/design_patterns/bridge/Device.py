# Define the Device class with methods to turn the device on and off
class Device:
    def __init__(self, id):
        self.id = id
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        print(f"Device {self.id} turned on.")

    def turn_off(self):
        self.state = "off"
        print(f"Device {self.id} turned off.")

# Define the RemoteControl class with a reference to a device and a method to press the button
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def press(self):
        if self.device.state == "off":
            self.device.turn_on()
        else:
            self.device.turn_off()

# Create instances of Device and RemoteControl
device1 = Device("bedroom_light")
device2 = Device("living_room_light")

remote_control1 = RemoteControl(device1)
remote_control2 = RemoteControl(device2)

# Press the remote control buttons to toggle the devices
remote_control1.press()  # Turns on the bedroom light
remote_control2.press()  # Turns on the living room light