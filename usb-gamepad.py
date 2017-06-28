from evdev import ecodes, InputDevice

gamepad = InputDevice('/dev/input/event0')
print(gamepad)
