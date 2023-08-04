'''
**High Level*: Algorithms and Data Structures

Category:
Design Patterns

Topic:
Mediator

Operation for 1st prompt (you only need to follow this for your 1st prompt):

Explain: Ask the assistant to explain a piece of code, and evaluate based on the quality of the explanations.

Subsequent Prompt Guidance (how you must continue your conversation past the first response):

(Conversation) Follow-up on previous responses: For all subsequent prompts, you must ask follow-ups,
 refinements, or clarifications specifically on previous responses or prompts. This should feel and sound like a
 CONVERSATION - follow-up prompts shouldn’t be able to stand on their own in a new conversation and receive the same response.
'''

# 1. Explain the following code:

class SmartHomeMediator:
    def __init__(self):
        self.devices = []

    def register_device(self, device):
        self.devices.append(device)

    def notify(self, device, event):
        for dev in self.devices:
            if dev != device:
                dev.handle_event(event)


class SmartDevice:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_event(self, event):
        self.mediator.notify(self, event)

    def handle_event(self, event):
        raise NotImplementedError


class Light(SmartDevice):
    def handle_event(self, event):
        if event == 'turn_on':
            print(f"{self.name} light turned on.")
        elif event == 'turn_off':
            print(f"{self.name} light turned off.")


class Thermostat(SmartDevice):
    def handle_event(self, event):
        if event == 'increase_temperature':
            print(f"{self.name} temperature increased.")
        elif event == 'decrease_temperature':
            print(f"{self.name} temperature decreased.")


class VoiceAssistant(SmartDevice):
    def handle_event(self, event):
        if event == 'play_music':
            print(f"{self.name} playing music.")
        elif event == 'dim_lights':
            print(f"{self.name} dimming lights.")


# Create the mediator
mediator = SmartHomeMediator()

# Create the smart devices and register them with the mediator
light = Light("Living Room", mediator)
thermostat = Thermostat("Bedroom", mediator)
voice_assistant = VoiceAssistant("Alexa", mediator)

mediator.register_device(light)
mediator.register_device(thermostat)
mediator.register_device(voice_assistant)

# Simulate user interactions
light.send_event('turn_on')
thermostat.send_event('increase_temperature')
voice_assistant.send_event('play_music')

'''
Here is the explanation of the code:

SmartHomeMediator is a class that contains a list of devices and handles registering and notifying devices of events.
SmartDevice is a base class for all smart devices, which contains a name property and a reference to its mediator.
Light, Thermostat, and VoiceAssistant are classes that inherit from SmartDevice and 
handle events specific to each device type. In this snippet, there is a SmartHomeMediator class that 
acts as a central intermediary to coordinate communication between smart devices. 
The mediator maintains a list of registered devices and provides methods for device registration and event notification.

The base class for all smart devices in the system is the SmartDevice class. Each smart appliance, like a light, 
a thermostat, and a voice assistant, extends the SmartDevice class, implementing the handle_event method to define its specific 
behavior when receiving events.

This calls the notify method internally, passing itself and the event as parameters. The mediator will then iterate 
over all of the registered devices and call their handle_event method, with the exception of the device that 
triggered the event.

In this code, we create instances of Light, Thermostat and VoiceAssistant, register them with the mediator and 
simulate user interactions by sending events to the devices. Each device handles the event and performs the associated 
action when an event is triggered.

Through the use of the Mediator design pattern, the smart home automation system achieves loose coupling between devices. 
The devices don’t need to know about each other explicitly, but they communicate through the Mediator, which allows for 
centralised control and coordination of the smart home functionality.
'''


# 2. What is the role of the SmartHomeMediator class in the code?

'''
The SmartHomeMediator class plays the role of a central intermediary that coordinates communication between smart devices. 
It maintains a list of registered devices and provides methods for device registration and event notification. When a device 
sends an event, the mediator notifies all the other devices except the device that triggered the event.

The mediator class allows devices to interact indirectly, reducing dependencies and promoting loose coupling. 
The mediator class allows devices to interact with each other in an indirect way, reducing direct dependencies and promoting 
a loose coupling between the devices. It enables seamless integration and coordination within the smart home ecosystem by 
providing a common interface for devices to register, communicate and receive events.
'''

# 3. What is the purpose of the handle_event method in the SmartDevice class?

'''
The handle_event method in the SmartDevice class is a virtual method that allows subclasses to handle events. 
This method is called by the notify method of the Mediator class when an event is triggered. The handle_event method 
is implemented by subclasses to handle events specific to the device type.

The purpose of the handle_event method in the SmartDevice class is to receive events from the mediator (SmartHomeMediator) 
and handle them based on the device's specific functionality. Each device may have different behaviors or actions to perform 
when certain events occur.

The handle_event method raises a NotImplementedError to indicate that the base class does not provide any implementation. 
The subclasses, such as Light, Thermostat, and VoiceAssistant, provide their implementation of the handle_event method 
to handle events specific to their functionality.

The device can define its own logic for handling events and responding to them by implementing the handle_event method 
in the SmartDevice class. Based on the events it receives, the device can interact with other devices or perform specific 
actions. The handle_event method acts as a callback which is invoked when the intermediary sends an event to the device.

The handle_event method is essential to provide the functionality of the smart home system. It allows the system to 
respond to user interactions by sending events to the appropriate devices, which will handle the events and perform 
the associated actions.
'''

# 4. Can multiple devices handle the same event simultaneously? Why or why not?

'''
Multiple devices can handle the same event simultaneously in this code. This is because the handle_event method is 
implemented in each device and they all have the same signature.

The SmartHomeMediator iterates over all registered devices and calls the handle_event method on each device when an 
event is triggered and dispatched. This way all devices that are subscribed to the event will be in receipt of the event 
at the same time.

Each device's handle_event method is executed independently and concurrently for each device handling the event. 
This allows a number of devices to respond to the same event at the same time and to perform their specific actions or 
operations based on the event.

```python
class SmartDevice:
def __init__(self, name, mediator):
    self.name = name
    self.mediator = mediator

def send_event(self, event):
    self.mediator.notify(self, event)

def handle_event(self, event):
    raise NotImplementedError


class Light(SmartDevice):
def handle_event(self, event):
    if event == 'turn_on':
        print(f"{self.name} light turned on.")
    elif event == 'turn_off':
        print(f"{self.name} light turned off.")


class Thermostat(SmartDevice):
def handle_event(self, event):
    if event == 'increase_temperature':
        print(f"{self.name} temperature increased.")
    elif event == 'decrease_temperature':
        print(f"{self.name} temperature decreased.")


class VoiceAssistant(SmartDevice):
def handle_event(self, event):
    if event == 'play_music':
        print(f"{self.name} playing music.")
    elif event == 'dim_lights':
        print(f"{self.name} dimming lights.")
```

However, it is important to note that this may not always be the intended behavior. It depends on the specific use 
case and requirements of the smart home system.

For example, consider a smart home system with a voice assistant and a light. When the user asks the voice assistant 
to play music, the system may want to dim the lights as well. In this case, both the voice assistant and the light will 
handle the same event simultaneously.

However, if the user asks the voice assistant to turn on the light, the system may want to prevent the light from being 
turned off simultaneously. In this case, only the voice assistant should handle the event.

To accommodate these use cases, the SmartHomeMediator class can keep a list of all the devices that handle a particular 
event. When an event is triggered, the Mediator can loop through the list of devices and call the handle_event method on 
each of them. This allows multiple devices to handle the same event simultaneously.

The Mediator design pattern makes it easy for devices to communicate and coordinate, but does not restrict how devices 
handle events. Each device can handle events concurrently and independently by having its own implementation of the 
handle_event method.
'''

# 5. How are events propagated and handled in this smart home automation system?

'''
Events are propagated and handled through the SmartHomeMediator class, which acts as a central intermediary for all 
the devices in the system.

When a device sends an event, the mediator notifies all the other devices except the device that triggered the event. 
The mediator iterates over all the registered devices and calls their handle_event method to handle the event.

The handle_event method is implemented in each device to handle events specific to that device. Each device can then 
perform the appropriate action based on the event it receives.

When an event occurs, such as a motion detected or a temperature change, the corresponding sensor or device detects 
the event and triggers it. The device then communicates the event to the SmartHomeMediator by calling its notify method, 
passing the event information as a parameter.

The SmartHomeMediator receives the event notification and performs the following steps:

1. It checks the type of event and identifies the devices that have an interest to handle that event. It does this 
through the maintenance of a registry of devices and the events to which they are subscribed.
2. This is done by iterating over the devices registered for the event and calling their handle_event method, passing 
the event info as a parameter.
3. Based on the event, each device that handles the event executes its own logic or operations. It could be to turn on 
the lights, adjust the temperature, play music, or do other things that automate your home.

For example, when the light sends an event to the mediator to turn on, the mediator notifies all the other devices, 
except the light, to handle the event. The thermostat may increase the temperature and the voice assistant may play music.

This way, the mediator allows the devices to communicate indirectly, reducing dependencies and promoting loose coupling.
'''