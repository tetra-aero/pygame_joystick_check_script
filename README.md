# pygame_joystick_check_script
This script is python, check to operation USB joystick with pygame lib..

## Install
```
sudo apt install joystick
sudo apt install python3-pygame
```

## How to use
- connect USB Joystick on Ubuntu 20.04

```
python3 ./pygame_joystick_check.py
```

### Example, result
```
$ python3 ./joystick_pygame_test.py 
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
Joystick Name: Generic X-Box pad
Number of Button : 11
Number of Axis : 6
Number of Hats : 1
HAT:0, 1
HAT:0, 0
HAT:-1, 0
HAT:0, 0
HAT:1, 0
......
......
JOYSTICK:[0.0, -0.01715087890625, 0.0, 0.0]
JOYSTICK:[0.0, -0.01715087890625, 0.0, 0.0]
JOYSTICK:[0.0, -0.01422119140625, 0.0, 0.0]
BUTTON:0
JOYSTICK:[0.0, -0.01116943359375, 0.0, 0.0]
JOYSTICK:[0.0, -0.01116943359375, 0.0, 0.0]
JOYSTICK:[0.0, -0.0078125, 0.0, 0.0]
JOYSTICK:[0.0, -0.0078125, 0.0, 0.0]
JOYSTICK:[0.0, -0.0078125, 0.0, 0.0]
JOYSTICK:[0.0, -0.001861572265625, 0.0, 0.0]
JOYSTICK:[0.0, -0.001861572265625, 0.0, 0.0]
JOYSTICK:[0.0, -0.001861572265625, 0.0, 0.0]
JOYSTICK:[0.0, -0.001739501953125, 0.0, 0.0]
BUTTON:0
JOYSTICK:[0.0, -0.00164794921875, 0.0, 0.0]
JOYSTICK:[0.0, -0.0015869140625, 0.0, 0.0]
BUTTON:1
BUTTON:2
BUTTON:3
BUTTON:4
BUTTON:5
BUTTON:7
BUTTON:6
BUTTON:8
JOYSTICK:[0.0, 0.0, 0.0, 0.0]
JOYSTICK:[0.0, 0.0, 0.0, 0.0]
JOYSTICK:[0.0, 0.001129150390625, 0.0, 0.0]
JOYSTICK:[0.0, 0.001129150390625, 0.0, 0.0]
JOYSTICK:[0.0, 0.001129150390625, 0.0, 0.0]
......
......
```

## I checked joystick
- Logitech Extream 3D Pro
- Generic Xbox Controller

## Other

### More easy way, jstest-gtk
```
sudo apt install jstest-gtk
jstest-gtk
```

### Example, Joystick Device Port
```
chiya@ujimatsu:~$ ls /dev/input/js0
/dev/input/js0
```

