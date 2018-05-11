# Installation

Requirements:

* pyevdev - Debian has a package `python3-evdev` 

Permission to the user to access to all the input devices:

```
useradd plugdev mte90
usermod -a -G plugdev mte90
```

Add the udev rules to your system `99-pydal.rules` on `/etc/udev/rules.d/`.