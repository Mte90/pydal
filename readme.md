# What?!?
[![License](https://img.shields.io/badge/License-BSD%20v3-blue.svg)](https://spdx.org/licenses/BSD-3-Clause)   
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FMte90%2Fpydal.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FMte90%2Fpydal?ref=badge_shield)


![](https://daniele.tech/wp-content/uploads/2018/05/footswitch-300x300.jpg)

As you can see in photo, in my case I have a foot switch and on Linux there is no official support by no one producer to configure it.  
Should be cool that every button execute a specific script (that do magic stuff of course) and not only a classic press event that print only `1`?  
With Python 3 and few permissions enabled this solution works on all the Linux distro.  

## Why

In my case I am using this footswitch to move the cursor between my 3 monitor to get the focus on the software opened at fullscreen that I usually have.  
THis is a very poor example but I want to get before experience (or remember that I have a pedal) and in the future use it for more advanced things.

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
Save the name of the keyboard that you want script somewhere.

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



## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FMte90%2Fpydal.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FMte90%2Fpydal?ref=badge_large)