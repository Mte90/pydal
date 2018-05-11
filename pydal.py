#!/usr/bin/python3
from evdev import InputDevice, categorize, ecodes, list_devices

print('Pydal started!')
devices = [InputDevice(fn) for fn in list_devices()]
print('Looking for the devices')
for device in devices:
    print(device)
    if device.name == 'MKEYBOARD':
        dev = InputDevice(device.fn)
        dev.grab()
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                press = categorize(event)
                if press.key_down:
                    print(press.keycode)
