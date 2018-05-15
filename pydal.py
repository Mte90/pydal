#!/usr/bin/python3
import configparser, argparse
from evdev import InputDevice, categorize, ecodes, list_devices


class C:
    pass


parameters = C()
parser = argparse.ArgumentParser(description='Pydal is a simple tool to change the behaviour of a bekyboard with scripts')
parser.add_argument('devices', help='The devices list', default=None)
parser.add_argument('run', help='Launch Pydal', default=None)
parser.add_argument('--config', help='Config file for Pydal', action='store_true', default=None)
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
parser.parse_args(['devices', 'run', '--config'], namespace=parameters)

print(parameters.devices)
if parameters.devices is not None or parameters.run is not None:
    print('Pydal started!')
    # Load configuration
    if parameters.config is not None:
        config = configparser.RawConfigParser()
        config.readfp(open(parameters.config))

    devices = [InputDevice(fn) for fn in list_devices()]
    print('Looking for the devices')
    for device in devices:
        if parameters.devices:
            print(device)
        if parameters.run:
            if device.name == 'MKEYBOARD':
                print('Device found!')
                dev = InputDevice(device.fn)
                dev.grab()
                for event in dev.read_loop():
                    if event.type == ecodes.EV_KEY:
                        press = categorize(event)
                        if press.key_down:
                            print(press.keycode)
else:
    parser.print_help()
