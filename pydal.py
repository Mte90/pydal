#!/usr/bin/python3
import configparser
import argparse
import os
import sys
import subprocess
import time
from evdev import InputDevice, categorize, ecodes, list_devices

parser = argparse.ArgumentParser(
    description="Pydal is a tiny script to assign a script to a button of a specific keyboard"
)
parser.add_argument("-devices", help="The devices list", nargs="?", action="store", const="1")
parser.add_argument("-run", help="Launch Pydal", nargs="?", action="store", const="1")
parser.add_argument("--config", help="Config file for Pydal", nargs="?", action="store", const="")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")
args = parser.parse_args()

if args.devices is None and args.run is None:
    parser.print_help()
    sys.exit()

print("Pydal started...")

config = configparser.RawConfigParser()
    
# Load configuration
config_path = './config.ini'
if args.config is not None:
    config_path = args.config

if not os.path.exists(config_path):
    print("Config file not found on " + config_path)
    exit()
print("  Config loaded!")
config.read_file(open(config_path))
hotkeys = {}
key = 0

for section in config.sections():
    if "key" in config[section]:
        key += 1
        hotkeys[config.get(section, "key")] = [config.get(section, "status"), config.get(section, "run")]
print("Find " + str(key) + " hotkeys to configure...")

last_pressed = {}
cooldown = 0.5

devices = [InputDevice(fn) for fn in reversed(list_devices())]
print("Looking for the devices...")
gotit = False
for device in devices:
    # Print devices
    if args.devices:
        print(device)

    # Read inputs and replace macros
    if args.run:
        if device.name == config.get("keyboard", "name"):
            gotit = True
            print("  Device found!")
            dev = InputDevice(device.path)
            try:
                dev.grab()
            except OSError:
                print("Device already grabbed!")
                sys.exit()
            for event in dev.read_loop():
                if event.type == ecodes.EV_KEY:
                    press = categorize(event)
                    button = press.keycode.replace("KEY_", "")
                    if button in hotkeys:
                        current_time = time.time()
                        last_time = last_pressed.get(button, 0)
                        if hotkeys[button][0] == "keyup" and press.key_up or hotkeys[button][0] == "keydown" and press.key_down:
                            if current_time - last_time >= cooldown:
                                print("Executing script for " + button + " on " + hotkeys[button][0])
                                subprocess.Popen(hotkeys[button][1], shell=True)
                                last_pressed[button] = current_time

if gotit is False and args.config is not None:
    print("  Device " + config.get("keyboard", "name") + " not found :-(")
