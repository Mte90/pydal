# What?!?

![](https://scontent-mxp1-1.cdninstagram.com/vp/24deea99016aa2194f65538dc11151dd/5B905E2E/t51.2885-15/e35/31412285_385252728550410_4628929324278349824_n.jpg)

AS YOu can see in photo, in my case is a foot switch but on Linux there is no support. Also can be cool to have that every button run a specific script that do magic and not a press event that print like `1`.  
With Python 3 and few permission enabled this solution works on all the linux distro.

# WIP

This is the first prototype version that has hardcoded the model name, the stable version will have a config for every button to execute a script in the state up/down.

# Installation

Requirements:

* pyevdev - Debian has a package `python3-evdev` 

Permission to the user to access to all the input devices:

```
useradd plugdev mte90
usermod -a -G plugdev mte90
```

Add the udev rules to your system `99-pydal.rules` on `/etc/udev/rules.d/`.

