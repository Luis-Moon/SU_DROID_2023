#!/usr/bin/env pybricks-micropython
from MODULOS.MOTORS import *
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()


andarParaFrente()
Choose()
andarParaFrente()
for i in range(1200, 0, -100):
    ev3.speaker.beep(i)
