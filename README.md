# omega2-python-evdev
python-evdev library for [Onion Omega2](https://onion.io/)

## Instructions

- ssh to your onion omega2
- download the package: `wget https://github.com/pleft/omega2-python-evdev/raw/master/packages/python-evdev_0.4.7-1_mipsel_24kc.ipk`
- install it: `opkg python-evdev_0.4.7-1_mipsel_24kc.ipk install`
- use it in your python scripts! For more: http://python-evdev.readthedocs.io

## usb-gamepad.py
Plug a usb joystick/gamepad on your onion [expansion dock](https://docs.onion.io/omega2-docs/expansion-dock.html). After a few seconds a new `device file` should appear in omega's `/dev/input` directory, usually named `event0`. `python-evdev` can read this device file and faciliates the translation of the events. 

For now `usb-gamepad.py` script just connects to `/dev/input/event0` and displays info about the joystick/gamepad controller connected to the usb port. It can be expanded to perform basic functions such as read the buttons' states.

Run it with: `python usb-gamepad.py`
