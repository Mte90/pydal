# Pydal
[![License](https://img.shields.io/badge/License-BSD%20v3-blue.svg)](https://spdx.org/licenses/BSD-3-Clause)

A simple way to create your macros, with a config file to execute cusom script/program and target a specific keyboard.

![](https://daniele.tech/wp-content/uploads/2018/05/footswitch-300x300.jpg)

As you can see in photo, in my case I have a foot switch and in this way I am able to use it to run scripts that move my mouse cursor in one of the 3 monitor I have.
This tiny Python script, parse the config file and map to the specific keyboard configured a script to execute on the various buttons.

# Configure

```
mte90:~/pydal $ ./pydal.py 
usage: pydal.py [-h] [-devices [DEVICES]] [-run [RUN]] [--config [CONFIG]]
                [--version]

Pydal is a simple tool to change the behaviour of a bekyboard with scripts on
Linux

optional arguments:
  -h, --help          show this help message and exit
  -devices [DEVICES]  The devices list
  -run [RUN]          Launch Pydal
  --config [CONFIG]   Config file for Pydal
  --version           show program's version number and exit
```

## First step

Run `pydal.py -devices` to get a list of all the HID devices connected to your computer.  
Save the name of the keyboard that you need to for your config file.

## Second step

Copy `config-sample.ini` where you want (also with a different name) and add the keyboard name in the config file.  
Configure the settings as you wish for every key, on the keydown/keyup status and a absolute path to the script that you want to execute.

## Third step

Run with `pydal.py --config /your/path/config.ini -run` and get fun!

# Installation

Requirements:

* pyevdev - Debian has a package `python3-evdev` 

Permission to the user to access to all the input devices:

```
useradd plugdev mte90
usermod -a -G plugdev mte90
```

Add the udev rules to your system `99-pydal.rules` on `/etc/udev/rules.d/`.
