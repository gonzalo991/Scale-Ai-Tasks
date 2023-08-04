class Device {
    constructor() {
        this.volume = 50;
        this.channel = 1;
        this.power = false;
    }

    isEnabled() {
        return this.power;
    };

    enable() {
        this.power = true;
    };

    disable() {
        this.power = false;
    };

    getVolume() {
        return this.volume;
    };

    setVolume(volume) {
        if (volume >= 0 && volume <= 100) {
            this.volume = volume;
        }
    };

    getChannel() {
        return this.channel;
    };

    setChannel(channel) {
        if (channel > 0) {
            this.channel = channel;
        }
    };
}

class Tv extends Device {
    switchToHdmi(input) {
        console.log(`Switched to HDMI input ${input}`);
    }
}

class Radio extends Device {
    setFrequency(frequency) {
        console.log(`Radio frequency set to ${frequency}`);
    }
}

class RemoteControl {
    constructor(device) {
        this.device = device;
    }

    togglePower() {
        if (this.device.isEnabled()) {
            this.device.disable();
        } else {
            this.device.enable();
        }
    }

    volumeDown() {
        this.device.setVolume(this.device.getVolume() - 10);
    }

    volumeUp() {
        this.device.setVolume(this.device.getVolume() + 10);
    }

    channelDown() {
        this.device.setChannel(this.device.getChannel() - 1);
    }

    channelUp() {
        this.device.setChannel(this.device.getChannel() + 1);
    }
}

class AdvancedRemoteControl extends RemoteControl {
    mute() {
        this.device.setVolume(0);
    }
}

let tv = new Tv();
let remote = new RemoteControl(tv);
remote.togglePower();
tv.switchToHdmi(1);

let radio = new Radio();
remote = new AdvancedRemoteControl(radio);
radio.setFrequency(101.2);
